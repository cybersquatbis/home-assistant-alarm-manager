"""Frontend registration for Alarme Manager Community."""

from __future__ import annotations

from pathlib import Path

from homeassistant.components import panel_custom
from homeassistant.components.frontend import async_remove_panel
from homeassistant.components.http import StaticPathConfig
from homeassistant.core import HomeAssistant

from .const import PANEL_URL, STATIC_URL

FRONTEND_DIR = Path(__file__).parent / "frontend"


async def async_register_frontend(hass: HomeAssistant) -> None:
    """Serve bundled assets and register the sidebar panel."""
    await hass.http.async_register_static_paths(
        [StaticPathConfig(STATIC_URL, str(FRONTEND_DIR), cache_headers=False)]
    )

    if PANEL_URL not in hass.data.get("frontend_panels", {}):
        await panel_custom.async_register_panel(
            hass=hass,
            frontend_url_path=PANEL_URL,
            webcomponent_name="alarme-manager-panel",
            module_url=f"{STATIC_URL}/alarme-manager-panel.js",
            sidebar_title="Alarme Manager",
            sidebar_icon="mdi:shield-home",
            require_admin=False,
        )


def async_unregister_frontend(hass: HomeAssistant) -> None:
    """Remove the sidebar panel."""
    if PANEL_URL in hass.data.get("frontend_panels", {}):
        async_remove_panel(hass, PANEL_URL)
