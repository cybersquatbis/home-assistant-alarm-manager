"""Persistent storage for Alarme Manager Community."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.helpers.storage import Store

from .const import MAX_INCIDENTS, STATIC_URL, STORAGE_KEY, STORAGE_VERSION

DEFAULT_DATA: dict[str, Any] = {
    "observation": True,
    "plan": {
        "image_url": f"{STATIC_URL}/plan_maison.svg",
        "markers": [],
    },
    "rules": {
        "lights_on_alarm": False,
        "siren_on_alarm": False,
        "capture_snapshots": False,
        "notify_on_incident": False,
    },
    "notification_profiles": [],
    "incidents": [],
}


class AlarmManagerStore:
    """Small wrapper around Home Assistant Store."""

    def __init__(self, hass: HomeAssistant) -> None:
        self._store = Store(hass, STORAGE_VERSION, STORAGE_KEY)
        self.data: dict[str, Any] = deepcopy(DEFAULT_DATA)

    async def async_load(self) -> dict[str, Any]:
        """Load and normalize stored data."""
        stored = await self._store.async_load()
        if isinstance(stored, dict):
            self.data = self._merge(deepcopy(DEFAULT_DATA), stored)
        return self.data

    async def async_save(self) -> None:
        """Persist current data."""
        await self._store.async_save(self.data)

    async def async_update(self, patch: dict[str, Any]) -> dict[str, Any]:
        """Merge a safe top-level patch and persist it."""
        allowed = {"observation", "plan", "rules", "notification_profiles"}
        clean_patch = {key: value for key, value in patch.items() if key in allowed}
        self.data = self._merge(self.data, clean_patch)
        await self.async_save()
        return self.data

    async def async_add_incident(self, incident: dict[str, Any]) -> None:
        """Add one incident, retaining only a bounded history."""
        incidents = self.data.setdefault("incidents", [])
        incidents.insert(0, incident)
        del incidents[MAX_INCIDENTS:]
        await self.async_save()

    async def async_clear_incidents(self) -> None:
        """Clear incident history."""
        self.data["incidents"] = []
        await self.async_save()

    @staticmethod
    def _merge(base: dict[str, Any], patch: dict[str, Any]) -> dict[str, Any]:
        for key, value in patch.items():
            if isinstance(value, dict) and isinstance(base.get(key), dict):
                base[key] = AlarmManagerStore._merge(base[key], value)
            else:
                base[key] = value
        return base
