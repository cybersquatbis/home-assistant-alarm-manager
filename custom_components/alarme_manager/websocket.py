"""WebSocket API for Alarme Manager Community."""
from __future__ import annotations
import voluptuous as vol
from homeassistant.components import websocket_api
from .const import *
def _runtime(hass):
    for v in hass.data.get(DOMAIN,{}).values():
        if isinstance(v,dict)and"engine"in v:return v
def _states(hass,ids):return{e:(hass.states[e].state if hass.states.get(e)else"unavailable")for e in(ids or[])}
@websocket_api.websocket_command({vol.Required("type"):f"{DOMAIN}/get_state"})
@websocket_api.async_response
async def get_state(hass,connection,msg):
    r=_runtime(hass)
    if not r:connection.send_result(msg["id"],{"configured":False});return
    e=r["engine"];s=r["store"];connection.send_result(msg["id"],{"configured":True,"observation":e.observation,"alarm_state":e.alarm_state,"incident_active":e.incident_active,"entities":e.config,"health":e.health(),"active_openings":e.active_entities(CONF_OPENINGS),"active_motions":e.active_entities(CONF_MOTIONS),"active_smoke":e.active_entities(CONF_SMOKE_ENTITIES),"temperature_states":_states(hass,e.config.get(CONF_TEMPERATURE_ENTITIES)),"data":s.data})
@websocket_api.websocket_command({vol.Required("type"):f"{DOMAIN}/save_panel_config",vol.Required("config"):dict})
@websocket_api.require_admin
@websocket_api.async_response
async def save_config(hass,connection,msg):
    r=_runtime(hass)
    if not r:connection.send_error(msg["id"],"not_configured","Alarme Manager is not configured");return
    connection.send_result(msg["id"],await r["store"].async_update(msg["config"]))
@websocket_api.websocket_command({vol.Required("type"):f"{DOMAIN}/clear_trace"})
@websocket_api.require_admin
@websocket_api.async_response
async def clear_trace(hass,connection,msg):
    r=_runtime(hass)
    if not r:connection.send_error(msg["id"],"not_configured","Alarme Manager is not configured");return
    await r["engine"].async_clear_trace();connection.send_result(msg["id"],{"ok":True})
def async_register_websocket_commands(hass):
    websocket_api.async_register_command(hass,get_state);websocket_api.async_register_command(hass,save_config);websocket_api.async_register_command(hass,clear_trace)
