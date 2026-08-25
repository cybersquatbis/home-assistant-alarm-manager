"""Constants for Alarme Manager Community."""
from typing import Final
DOMAIN: Final = "alarme_manager"
NAME: Final = "Alarme Manager Community"
VERSION: Final = "0.4.0-beta.1"
PANEL_URL: Final = "alarme-manager"
STATIC_URL: Final = "/alarme_manager_static"
STORAGE_KEY: Final = "alarme_manager.storage"
STORAGE_VERSION: Final = 2
SIGNAL_UPDATE: Final = f"{DOMAIN}_update"
CONF_NAME="name"; CONF_ALARM_ENTITY="alarm_entity"; CONF_OPENINGS="openings"; CONF_MOTIONS="motions"; CONF_SMOKE_ENTITIES="smoke_entities"; CONF_CAMERAS="cameras"; CONF_LIGHTS="lights"; CONF_AUX_DEVICES="aux_devices"; CONF_SIREN="siren"; CONF_CRITICAL_ENTITIES="critical_entities"; CONF_RF_ENTITIES="rf_entities"; CONF_RAIN_ENTITY="rain_entity"; CONF_SIREN_DURATION="siren_duration"; CONF_TEMPERATURE_ENTITIES="temperature_entities"
DEFAULT_NAME="Maison"; DEFAULT_SIREN_DURATION=30; MAX_INCIDENTS=100; MAX_TEST_DURATION=10; MAX_TRACE_POINTS=100
PLATFORMS=["sensor"]
