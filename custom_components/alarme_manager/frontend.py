"""Frontend registration for Alarme Manager Community."""
from __future__ import annotations
from pathlib import Path
from homeassistant.components import panel_custom
from homeassistant.components.frontend import async_remove_panel
from homeassistant.components.http import StaticPathConfig
from .const import PANEL_URL,STATIC_URL
ASSET_DIR=Path(__file__).parent
async def async_register_frontend(hass):
    await hass.http.async_register_static_paths([StaticPathConfig(STATIC_URL,str(ASSET_DIR),cache_headers=False)])
    if PANEL_URL not in hass.data.get("frontend_panels",{}):
        await panel_custom.async_register_panel(hass=hass,frontend_url_path=PANEL_URL,webcomponent_name="alarme-manager-panel",module_url=f"{STATIC_URL}/community-0.5.js",sidebar_title="Alarme Manager",sidebar_icon="mdi:shield-home",require_admin=False)
def async_unregister_frontend(hass):
    if PANEL_URL in hass.data.get("frontend_panels",{}):async_remove_panel(hass,PANEL_URL)
