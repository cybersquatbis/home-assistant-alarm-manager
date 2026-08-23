"""Binary sensors for Alarme Manager Community."""

from __future__ import annotations

from homeassistant.components.binary_sensor import BinarySensorDeviceClass, BinarySensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, SIGNAL_UPDATE


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    engine = hass.data[DOMAIN][entry.entry_id]["engine"]
    async_add_entities(
        [AlarmManagerProblemSensor(engine, entry), AlarmManagerIncidentSensor(engine, entry)]
    )


class AlarmManagerBaseBinarySensor(BinarySensorEntity):
    _attr_has_entity_name = True

    def __init__(self, engine, entry: ConfigEntry, key: str, name: str) -> None:
        self.engine = engine
        self._attr_unique_id = f"{entry.entry_id}_{key}"
        self._attr_name = name
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


class AlarmManagerProblemSensor(AlarmManagerBaseBinarySensor):
    _attr_device_class = BinarySensorDeviceClass.PROBLEM
    _attr_icon = "mdi:shield-alert"

    def __init__(self, engine, entry: ConfigEntry) -> None:
        super().__init__(engine, entry, "problem", "Problème de supervision")

    @property
    def is_on(self) -> bool:
        return not self.engine.health()["healthy"]

    @property
    def extra_state_attributes(self):
        return self.engine.health()


class AlarmManagerIncidentSensor(AlarmManagerBaseBinarySensor):
    _attr_device_class = BinarySensorDeviceClass.SAFETY
    _attr_icon = "mdi:alarm-light"

    def __init__(self, engine, entry: ConfigEntry) -> None:
        super().__init__(engine, entry, "incident_active", "Incident actif")

    @property
    def is_on(self) -> bool:
        return self.engine.incident_active
