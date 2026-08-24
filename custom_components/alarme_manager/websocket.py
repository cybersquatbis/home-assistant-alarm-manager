"""WebSocket API for the Alarme Manager panel."""
from __future__ import annotations
from typing import Any
import voluptuous as vol
from homeassistant.components import websocket_api
from homeassistant.core import HomeAssistant
from .const import DOMAIN, CONF_AUX_DEVICES, CONF_LIGHTS, CONF_SMOKE_ENTITIES


def _runtime(hass: HomeAssistant) -> dict[str, Any] | None:
    for value in hass.data.get(DOMAIN, {}).values():
        if isinstance(value, dict) and "engine" in value: return value
    return None


def _states(hass, ids):
    result={}
    for eid in ids or []:
        st=hass.states.get(eid)
        result[eid]=st.state if st else "unavailable"
    return result

@websocket_api.websocket_command({vol.Required("type"): f"{DOMAIN}/get_state"})
@websocket_api.async_response
async def websocket_get_state(hass, connection, msg) -> None:
    runtime=_runtime(hass)
    if runtime is None:
        connection.send_result(msg["id"], {"configured": False}); return
    engine=runtime["engine"]; store=runtime["store"]
    connection.send_result(msg["id"],{
        "configured":True,"observation":engine.observation,"alarm_state":engine.alarm_state,
        "incident_active":engine.incident_active,"entities":engine.config,"health":engine.health(),
        "active_openings":engine.active_entities("openings"),"active_motions":engine.active_entities("motions"),
        "active_smoke":engine.active_entities(CONF_SMOKE_ENTITIES),
        "light_states":_states(hass,engine.config.get(CONF_LIGHTS)),
        "aux_states":_states(hass,engine.config.get(CONF_AUX_DEVICES)),
        "smoke_states":_states(hass,engine.config.get(CONF_SMOKE_ENTITIES)),"data":store.data})

@websocket_api.websocket_command({vol.Required("type"): f"{DOMAIN}/save_panel_config",vol.Required("config"):dict})
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_save_panel_config(hass, connection, msg) -> None:
    runtime=_runtime(hass)
    if runtime is None:
        connection.send_error(msg["id"],"not_configured","Alarme Manager is not configured"); return
    connection.send_result(msg["id"],await runtime["store"].async_update(msg["config"]))

def async_register_websocket_commands(hass: HomeAssistant) -> None:
    websocket_api.async_register_command(hass,websocket_get_state); websocket_api.async_register_command(hass,websocket_save_panel_config)
