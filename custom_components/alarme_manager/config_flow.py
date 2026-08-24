"""Config flow for Alarme Manager Community."""

from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.config_entries import ConfigFlowResult
from homeassistant.core import callback
from homeassistant.helpers import selector

from .const import (
    CONF_ALARM_ENTITY,
    CONF_AUX_DEVICES,
    CONF_CAMERAS,
    CONF_CRITICAL_ENTITIES,
    CONF_LIGHTS,
    CONF_MOTIONS,
    CONF_NAME,
    CONF_OPENINGS,
    CONF_RAIN_ENTITY,
    CONF_RF_ENTITIES,
    CONF_SIREN,
    CONF_SIREN_DURATION,
    CONF_SMOKE_ENTITIES,
    DEFAULT_NAME,
    DEFAULT_SIREN_DURATION,
    DOMAIN,
)


def _entity_selector(domain: str | None = None, multiple: bool = False):
    config: dict[str, Any] = {"multiple": multiple}
    if domain:
        config["filter"] = {"domain": domain}
    return selector.EntitySelector(selector.EntitySelectorConfig(**config))


def _schema(defaults: dict[str, Any]) -> vol.Schema:
    return vol.Schema(
        {
            vol.Optional(CONF_NAME, default=defaults.get(CONF_NAME, DEFAULT_NAME)): selector.TextSelector(),
            vol.Optional(CONF_ALARM_ENTITY, default=defaults.get(CONF_ALARM_ENTITY)): _entity_selector("alarm_control_panel"),
            vol.Optional(CONF_OPENINGS, default=defaults.get(CONF_OPENINGS, [])): _entity_selector(multiple=True),
            vol.Optional(CONF_MOTIONS, default=defaults.get(CONF_MOTIONS, [])): _entity_selector(multiple=True),
            vol.Optional(CONF_SMOKE_ENTITIES, default=defaults.get(CONF_SMOKE_ENTITIES, [])): _entity_selector("binary_sensor", multiple=True),
            vol.Optional(CONF_CAMERAS, default=defaults.get(CONF_CAMERAS, [])): _entity_selector("camera", multiple=True),
            vol.Optional(CONF_LIGHTS, default=defaults.get(CONF_LIGHTS, [])): _entity_selector(multiple=True),
            vol.Optional(CONF_AUX_DEVICES, default=defaults.get(CONF_AUX_DEVICES, [])): _entity_selector(multiple=True),
            vol.Optional(CONF_SIREN, default=defaults.get(CONF_SIREN)): _entity_selector(),
            vol.Optional(CONF_SIREN_DURATION, default=defaults.get(CONF_SIREN_DURATION, DEFAULT_SIREN_DURATION)): selector.NumberSelector(
                selector.NumberSelectorConfig(min=1, max=300, step=1, mode=selector.NumberSelectorMode.BOX)
            ),
            vol.Optional(CONF_CRITICAL_ENTITIES, default=defaults.get(CONF_CRITICAL_ENTITIES, [])): _entity_selector(multiple=True),
            vol.Optional(CONF_RF_ENTITIES, default=defaults.get(CONF_RF_ENTITIES, [])): _entity_selector(multiple=True),
            vol.Optional(CONF_RAIN_ENTITY, default=defaults.get(CONF_RAIN_ENTITY)): _entity_selector(),
        }
    )


class AlarmManagerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle the initial config flow."""

    VERSION = 1

    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult:
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")
        if user_input is not None:
            title = user_input.get(CONF_NAME) or DEFAULT_NAME
            return self.async_create_entry(title=title, data=user_input)
        return self.async_show_form(step_id="user", data_schema=_schema({}))

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: config_entries.ConfigEntry):
        return AlarmManagerOptionsFlow()


class AlarmManagerOptionsFlow(config_entries.OptionsFlow):
    """Edit supervised entities from Home Assistant UI."""

    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult:
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)
        defaults = {**self.config_entry.data, **self.config_entry.options}
        return self.async_show_form(step_id="init", data_schema=_schema(defaults))
