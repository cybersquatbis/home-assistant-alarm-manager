"""Event-driven supervision engine for Alarme Manager Community."""
from __future__ import annotations
from datetime import datetime
from pathlib import Path
from homeassistant.const import STATE_UNAVAILABLE,STATE_UNKNOWN
from homeassistant.helpers.dispatcher import async_dispatcher_send
from homeassistant.helpers.event import async_call_later,async_track_state_change_event
from homeassistant.core import callback
from .const import *
ACTIVE={"on","open","opening","detected","motion","problem","jammed","heat","heating","active","running","occupied"}
class AlarmManagerEngine:
    def __init__(self,hass,entry,store): self.hass=hass;self.entry=entry;self.store=store;self._remove=None;self._reacting=False
    @property
    def config(self): return {**self.entry.data,**self.entry.options}
    @property
    def observation(self): return bool(self.store.data.get("observation",True))
    @property
    def alarm_state(self):
        eid=self.config.get(CONF_ALARM_ENTITY);st=self.hass.states.get(eid) if eid else None;return st.state if st else None
    @property
    def incident_active(self): return self.alarm_state=="triggered"
    async def async_start(self):
        await self.store.async_load();ids=sorted(self.all_configured_entities())
        if ids:self._remove=async_track_state_change_event(self.hass,ids,self._changed)
        async_dispatcher_send(self.hass,SIGNAL_UPDATE)
    async def async_stop(self):
        if self._remove:self._remove();self._remove=None
    def all_configured_entities(self):
        c=self.config;out=set()
        for k in (CONF_OPENINGS,CONF_MOTIONS,CONF_SMOKE_ENTITIES,CONF_TEMPERATURE_ENTITIES,CONF_CAMERAS,CONF_LIGHTS,CONF_AUX_DEVICES,CONF_CRITICAL_ENTITIES,CONF_RF_ENTITIES):out.update(x for x in(c.get(k)or[])if isinstance(x,str))
        for k in(CONF_ALARM_ENTITY,CONF_SIREN):
            if isinstance(c.get(k),str)and c[k]:out.add(c[k])
        return out
    async def _changed(self,event):
        eid=event.data.get("entity_id");new=event.data.get("new_state");old=event.data.get("old_state")
        if not new:return
        became=new.state.lower() in ACTIVE and(not old or old.state.lower()not in ACTIVE)
        if became and(eid in(self.config.get(CONF_MOTIONS)or[])or eid in(self.config.get(CONF_OPENINGS)or[])):await self._trace(eid,"motion"if eid in(self.config.get(CONF_MOTIONS)or[])else"opening")
        if eid==self.config.get(CONF_ALARM_ENTITY)and new.state=="triggered"and(not old or old.state!="triggered"):await self.async_record_incident("alarm",eid);await self._reactions()
        if eid in(self.config.get(CONF_SMOKE_ENTITIES)or[])and became:await self.async_record_incident("smoke",eid)
        async_dispatcher_send(self.hass,SIGNAL_UPDATE)
    async def _trace(self,eid,kind):
        p=self.store.data.get("plan",{});trace=self.store.data.setdefault("trace",[]);now=datetime.now().astimezone()
        if trace:
            try:
                if(now-datetime.fromisoformat(trace[-1]["time"])).total_seconds()>int(p.get("trace_reset_seconds",300)):trace.clear()
            except Exception:pass
        if kind=="opening"and not p.get("trace_include_openings",True):return
        marker=next((m for m in p.get("markers",[])if m.get("entity_id")==eid),{});trace.append({"entity_id":eid,"kind":kind,"label":marker.get("label")or self._friendly(eid),"x":marker.get("x",50),"y":marker.get("y",50),"time":now.isoformat()});del trace[:-MAX_TRACE_POINTS];await self.store.async_save()
    def _friendly(self,eid):
        st=self.hass.states.get(eid);return(st.attributes.get("friendly_name")if st else None)or eid
    def active_entities(self,key):return[e for e in(self.config.get(key)or[])if(self.hass.states.get(e)and self.hass.states[e].state.lower()in ACTIVE)]
    def health(self):
        ids=sorted(self.all_configured_entities());un=[e for e in ids if not self.hass.states.get(e)or self.hass.states[e].state in{STATE_UNAVAILABLE,STATE_UNKNOWN}];rf=[e for e in(self.config.get(CONF_RF_ENTITIES)or[])if(not self.hass.states.get(e)or self.hass.states[e].state in{STATE_UNAVAILABLE,STATE_UNKNOWN}or self.hass.states[e].state.lower()in ACTIVE)];return{"score":round(100*(len(ids)-len(un))/len(ids))if ids else 0,"supervised":ids,"unavailable":un,"rf_alerts":rf,"healthy":not un and not rf}
    async def async_set_observation(self,enabled):await self.store.async_update({"observation":bool(enabled)});async_dispatcher_send(self.hass,SIGNAL_UPDATE)
    async def async_clear_trace(self):await self.store.async_set_trace([]);async_dispatcher_send(self.hass,SIGNAL_UPDATE)
    async def async_record_incident(self,kind,trigger_entity=None,note=None):
        i={"time":datetime.now().astimezone().isoformat(),"kind":kind,"trigger_entity":trigger_entity,"note":note,"observation":self.observation,"alarm_state":self.alarm_state,"openings":self.active_entities(CONF_OPENINGS),"motions":self.active_entities(CONF_MOTIONS),"smoke":self.active_entities(CONF_SMOKE_ENTITIES),"snapshots":[]};await self.store.async_add_incident(i);async_dispatcher_send(self.hass,SIGNAL_UPDATE);return i
    async def _reactions(self):
        if self.observation or self._reacting:return
        self._reacting=True
        try:
            r=self.store.data.get("rules",{})
            if r.get("capture_snapshots"):await self._snapshots()
            if r.get("notify_on_incident"):await self._notify()
            if r.get("lights_on_alarm")and self.config.get(CONF_LIGHTS):await self.hass.services.async_call("homeassistant","turn_on",{"entity_id":self.config[CONF_LIGHTS]},blocking=False)
            if r.get("siren_on_alarm")and self.config.get(CONF_SIREN):await self._siren()
        finally:self._reacting=False
    async def _siren(self):
        eid=self.config[CONF_SIREN];await self.hass.services.async_call("homeassistant","turn_on",{"entity_id":eid},blocking=False)
        @callback
        def off(_):self.hass.async_create_task(self.hass.services.async_call("homeassistant","turn_off",{"entity_id":eid},blocking=False))
        async_call_later(self.hass,max(1,min(int(self.config.get(CONF_SIREN_DURATION,DEFAULT_SIREN_DURATION)),300)),off)
    async def _snapshots(self):
        d=Path(self.hass.config.path("www","alarme_manager"));d.mkdir(parents=True,exist_ok=True);urls=[];stamp=datetime.now().strftime("%Y%m%d-%H%M%S")
        for eid in self.config.get(CONF_CAMERAS,[])or[]:
            f=d/f"{stamp}-{eid.replace('.','_')}.jpg"
            try:await self.hass.services.async_call("camera","snapshot",{"entity_id":eid,"filename":str(f)},blocking=True);urls.append(f"/local/alarme_manager/{f.name}")
            except Exception:pass
        if urls and self.store.data.get("incidents"):self.store.data["incidents"][0]["snapshots"]=urls;await self.store.async_save()
    async def _notify(self):
        for p in self.store.data.get("notification_profiles",[])or[]:
            if isinstance(p,dict)and p.get("service")and p.get("alerts",True):
                try:await self.hass.services.async_call("notify",p["service"],{"title":"Alarme Manager","message":"Incident détecté. Consultez Alarme Manager."},blocking=False)
                except Exception:pass
