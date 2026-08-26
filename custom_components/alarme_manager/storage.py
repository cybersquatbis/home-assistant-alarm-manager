"""Persistent storage for Alarme Manager Community."""
from __future__ import annotations
from copy import deepcopy
from typing import Any
from homeassistant.helpers.storage import Store
from .const import MAX_INCIDENTS,STORAGE_KEY,STORAGE_VERSION
DEFAULT_DATA:dict[str,Any]={"observation":True,"plan":{"image_url":"","markers":[],"entity_scales":{"global":100,"opening":100,"motion":100,"smoke":100,"camera":100,"light":100,"aux":100,"siren":100,"rf":100,"critical":100,"temperature":100},"trace_enabled":True,"trace_include_openings":True,"trace_reset_seconds":300},"rules":{"lights_on_alarm":False,"siren_on_alarm":False,"capture_snapshots":False,"notify_on_incident":False,"require_opening_before_reactions":True,"opening_confirmation_window":120},"notification_profiles":[],"incidents":[],"trace":[]}
class AlarmManagerStore:
    def __init__(self,hass): self._store=Store(hass,STORAGE_VERSION,STORAGE_KEY);self.data=deepcopy(DEFAULT_DATA)
    async def async_load(self):
        stored=await self._store.async_load()
        if isinstance(stored,dict): self.data=self._merge(deepcopy(DEFAULT_DATA),stored)
        return self.data
    async def async_save(self): await self._store.async_save(self.data)
    async def async_update(self,patch):
        allowed={"observation","plan","rules","notification_profiles","trace"};self.data=self._merge(self.data,{k:v for k,v in patch.items() if k in allowed});await self.async_save();return self.data
    async def async_add_incident(self,incident):
        rows=self.data.setdefault("incidents",[]);rows.insert(0,incident);del rows[MAX_INCIDENTS:];await self.async_save()
    async def async_clear_incidents(self): self.data["incidents"]=[];await self.async_save()
    async def async_set_trace(self,trace): self.data["trace"]=trace;await self.async_save()
    @staticmethod
    def _merge(base,patch):
        for k,v in patch.items():
            if isinstance(v,dict) and isinstance(base.get(k),dict): base[k]=AlarmManagerStore._merge(base[k],v)
            else: base[k]=v
        return base
