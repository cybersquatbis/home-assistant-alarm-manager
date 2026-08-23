"""Alarme Manager Community integration."""

from __future__ import annotations

import logging

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall, callback
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.dispatcher import async_dispatcher_send
from homeassistant.helpers.event import async_call_later

from .const import DOMAIN, MAX_TEST_DURATION, PLATFORMS, SIGNAL_UPDATE
from .engine import AlarmManagerEngine
from .frontend import async_register_frontend
from .storage import AlarmManagerStore
from .websocket import async_register_websocket_commands

_LOGGER = logging.getLogger(__name__)

SET_MODE_SCHEMA = vol.Schema(
    {
        vol.Required("mode"): vol.In(["observation", "active"]),
        vol.Optional("confirm", default=False): cv.boolean,
    }
)
SIMULATE_SCHEMA = vol.Schema(
    {
        vol.Optional("note", default="Test utilisateur"): cv.string,
    }
)
TEST_OUTPUT_SCHEMA = vol.Schema(
    {
        vol.Required("kind"): vol.In(["light", "siren"]),
        vol.Required("entity_id"): cv.entity_id,
        vol.Optional("duration", default=3): vol.All(vol.Coerce(int), vol.Range(min=1, max=MAX_TEST_DURATION)),
        vol.Optional("confirm", default=False): cv.boolean,
    }
)


def _first_runtime(hass: HomeAssistant):
    for value in hass.data.get(DOMAIN, {}).values():
        if isinstance(value, dict) and "engine" in value:
            return value
    return None


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up global integration services and frontend."""
    hass.data.setdefault(DOMAIN, {})
    async_register_websocket_commands(hass)
    await async_register_frontend(hass)

    async def _set_mode(call: ServiceCall) -> None:
        runtime = _first_runtime(hass)
        if runtime is None:
            raise HomeAssistantError("Alarme Manager n'est pas configuré")
        mode = call.data["mode"]
        if mode == "active" and not call.data.get("confirm"):
            raise HomeAssistantError(
                "Le passage en mode ACTIF exige confirm: true afin d'éviter une activation accidentelle."
            )
        await runtime["engine"].async_set_observation(mode == "observation")

    async def _simulate(call: ServiceCall) -> None:
        runtime = _first_runtime(hass)
        if runtime is None:
            raise HomeAssistantError("Alarme Manager n'est pas configuré")
        await runtime["engine"].async_record_incident("simulation", note=call.data.get("note"))

    async def _clear_history(call: ServiceCall) -> None:
        runtime = _first_runtime(hass)
        if runtime is None:
            raise HomeAssistantError("Alarme Manager n'est pas configuré")
        await runtime["store"].async_clear_incidents()
        async_dispatcher_send(hass, SIGNAL_UPDATE)

    async def _test_output(call: ServiceCall) -> None:
        if not call.data.get("confirm"):
            raise HomeAssistantError("Le test exige confirm: true")
        entity_id = call.data["entity_id"]
        kind = call.data["kind"]
        duration = call.data["duration"]
        domain = "light" if kind == "light" else "homeassistant"
        await hass.services.async_call(domain, "turn_on", {"entity_id": entity_id}, blocking=True)

        @callback
        def _turn_off(_now) -> None:
            hass.async_create_task(
                hass.services.async_call(domain, "turn_off", {"entity_id": entity_id}, blocking=False)
            )

        async_call_later(hass, duration, _turn_off)

    hass.services.async_register(DOMAIN, "set_mode", _set_mode, schema=SET_MODE_SCHEMA)
    hass.services.async_register(DOMAIN, "simulate_incident", _simulate, schema=SIMULATE_SCHEMA)
    hass.services.async_register(DOMAIN, "clear_history", _clear_history)
    hass.services.async_register(DOMAIN, "test_output", _test_output, schema=TEST_OUTPUT_SCHEMA)
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Alarme Manager from a config entry."""
    store = AlarmManagerStore(hass)
    engine = AlarmManagerEngine(hass, entry, store)
    await engine.async_start()

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = {
        "store": store,
        "engine": engine,
    }

    entry.async_on_unload(entry.add_update_listener(async_reload_entry))
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    runtime = hass.data.get(DOMAIN, {}).get(entry.entry_id)
    if runtime:
        await runtime["engine"].async_stop()

    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data.get(DOMAIN, {}).pop(entry.entry_id, None)
    return unload_ok


async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload after options are changed."""
    await hass.config_entries.async_reload(entry.entry_id)
