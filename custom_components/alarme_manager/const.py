"""Constants for Alarme Manager Community."""

from __future__ import annotations

from typing import Final

DOMAIN: Final = "alarme_manager"
NAME: Final = "Alarme Manager Community"
VERSION: Final = "0.2.0-beta.1"

PANEL_URL: Final = "alarme-manager"
STATIC_URL: Final = "/alarme_manager_static"
STORAGE_KEY: Final = "alarme_manager.storage"
STORAGE_VERSION: Final = 1
SIGNAL_UPDATE: Final = f"{DOMAIN}_update"

CONF_NAME: Final = "name"
CONF_ALARM_ENTITY: Final = "alarm_entity"
CONF_OPENINGS: Final = "openings"
CONF_MOTIONS: Final = "motions"
CONF_SMOKE_ENTITIES: Final = "smoke_entities"
CONF_CAMERAS: Final = "cameras"
CONF_LIGHTS: Final = "lights"
CONF_SIREN: Final = "siren"
CONF_CRITICAL_ENTITIES: Final = "critical_entities"
CONF_RF_ENTITIES: Final = "rf_entities"
CONF_RAIN_ENTITY: Final = "rain_entity"
CONF_SIREN_DURATION: Final = "siren_duration"

DEFAULT_NAME: Final = "Maison"
DEFAULT_SIREN_DURATION: Final = 30
MAX_INCIDENTS: Final = 100
MAX_TEST_DURATION: Final = 10

PLATFORMS: Final = ["sensor", "binary_sensor"]
