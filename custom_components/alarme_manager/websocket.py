"""WebSocket API for the Alarme Manager panel."""

from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant.components import websocket_api
from homeassistant.core import HomeAssistant

from .const import DOMAIN


def _runtime(hass: HomeAssistant) -> dict[str, Any] | None:
    domain_data = hass.data.get(DOMAIN, {})
    for value in domain_data.values():
        if isinstance(value, dict) and "engine" in value:
            return value
    return None


@websocket_api.websocket_command({vol.Required("type"): f"{DOMAIN}/get_state"})
@websocket_api.async_response
async def websocket_get_state(hass, connection, msg) -> None:
    """Return current integration state and persistent panel data."""
    runtime = _runtime(hass)
    if runtime is None:
        connection.send_result(msg["id"], {"configured": False})
        return

    engine = runtime["engine"]
    store = runtime["store"]
    connection.send_result(
        msg["id"],
        {
            "configured": True,
            "observation": engine.observation,
            "alarm_state": engine.alarm_state,
            "incident_active": engine.incident_active,
            "entities": engine.config,
            "health": engine.health(),
            "active_openings": engine.active_entities("openings"),
            "active_motions": engine.active_entities("motions"),
            "data": store.data,
        },
    )


@websocket_api.websocket_command(
    {
        vol.Required("type"): f"{DOMAIN}/save_panel_config",
        vol.Required("config"): dict,
    }
)
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_save_panel_config(hass, connection, msg) -> None:
    """Persist plan, rules and notification profile configuration."""
    runtime = _runtime(hass)
    if runtime is None:
        connection.send_error(msg["id"], "not_configured", "Alarme Manager is not configured")
        return
    data = await runtime["store"].async_update(msg["config"])
    connection.send_result(msg["id"], data)


def async_register_websocket_commands(hass: HomeAssistant) -> None:
    """Register all WebSocket commands once."""
    websocket_api.async_register_command(hass, websocket_get_state)
    websocket_api.async_register_command(hass, websocket_save_panel_config)
