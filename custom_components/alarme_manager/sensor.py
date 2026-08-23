"""Sensors for Alarme Manager Community."""

from __future__ import annotations

from datetime import datetime

from homeassistant.components.sensor import SensorDeviceClass, SensorEntity, SensorEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, SIGNAL_UPDATE


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    runtime = hass.data[DOMAIN][entry.entry_id]
    engine = runtime["engine"]
    async_add_entities(
        [
            AlarmManagerScoreSensor(engine, entry),
            AlarmManagerModeSensor(engine, entry),
            AlarmManagerLastIncidentSensor(engine, entry),
        ]
    )


class AlarmManagerBaseSensor(SensorEntity):
    _attr_has_entity_name = True

    def __init__(self, engine, entry: ConfigEntry, description: SensorEntityDescription) -> None:
        self.engine = engine
        self.entity_description = description
        self._attr_unique_id = f"{entry.entry_id}_{description.key}"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, entry.entry_id)},
            "name": "Alarme Manager",
            "manufacturer": "Community",
            "model": "Security supervisor",
        }

    async def async_added_to_hass(self) -> None:
        self.async_on_remove(
            async_dispatcher_connect(self.hass, SIGNAL_UPDATE, self.async_write_ha_state)
        )


class AlarmManagerScoreSensor(AlarmManagerBaseSensor):
    def __init__(self, engine, entry: ConfigEntry) -> None:
        super().__init__(
            engine,
            entry,
            SensorEntityDescription(
                key="protection_score",
                name="Score de protection",
                icon="mdi:shield-check",
                native_unit_of_measurement="%",
            ),
        )

    @property
    def native_value(self):
        return self.engine.health()["score"]

    @property
    def extra_state_attributes(self):
        health = self.engine.health()
        return {
            "unavailable": health["unavailable"],
            "rf_alerts": health["rf_alerts"],
            "supervised_count": len(health["supervised"]),
        }


class AlarmManagerModeSensor(AlarmManagerBaseSensor):
    def __init__(self, engine, entry: ConfigEntry) -> None:
        super().__init__(
            engine,
            entry,
            SensorEntityDescription(key="mode", name="Mode", icon="mdi:eye-outline"),
        )

    @property
    def native_value(self):
        return "observation" if self.engine.observation else "active"


class AlarmManagerLastIncidentSensor(AlarmManagerBaseSensor):
    def __init__(self, engine, entry: ConfigEntry) -> None:
        super().__init__(
            engine,
            entry,
            SensorEntityDescription(key="last_incident", name="Dernier incident", icon="mdi:history", device_class=SensorDeviceClass.TIMESTAMP),
        )

    @property
    def native_value(self):
        incidents = self.engine.store.data.get("incidents", [])
        if not incidents:
            return None
        try:
            return datetime.fromisoformat(incidents[0]["time"])
        except (KeyError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        incidents = self.engine.store.data.get("incidents", [])
        return incidents[0] if incidents else {}
