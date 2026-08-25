"""Config flow for Alarme Manager Community."""
from __future__ import annotations
from typing import Any
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import selector
from .const import *

def _entity(domain=None,multiple=False):
    cfg={"multiple":multiple}
    if domain: cfg["filter"]={"domain":domain}
    return selector.EntitySelector(selector.EntitySelectorConfig(**cfg))

def _schema(d):
    return vol.Schema({
        vol.Optional(CONF_NAME,default=d.get(CONF_NAME,DEFAULT_NAME)): selector.TextSelector(),
        vol.Optional(CONF_ALARM_ENTITY,default=d.get(CONF_ALARM_ENTITY)): _entity("alarm_control_panel"),
        vol.Optional(CONF_OPENINGS,default=d.get(CONF_OPENINGS,[])): _entity(multiple=True),
        vol.Optional(CONF_MOTIONS,default=d.get(CONF_MOTIONS,[])): _entity("binary_sensor",True),
        vol.Optional(CONF_SMOKE_ENTITIES,default=d.get(CONF_SMOKE_ENTITIES,[])): _entity("binary_sensor",True),
        vol.Optional(CONF_TEMPERATURE_ENTITIES,default=d.get(CONF_TEMPERATURE_ENTITIES,[])): _entity("sensor",True),
        vol.Optional(CONF_CAMERAS,default=d.get(CONF_CAMERAS,[])): _entity("camera",True),
        vol.Optional(CONF_LIGHTS,default=d.get(CONF_LIGHTS,[])): _entity(multiple=True),
        vol.Optional(CONF_AUX_DEVICES,default=d.get(CONF_AUX_DEVICES,[])): _entity(multiple=True),
        vol.Optional(CONF_SIREN,default=d.get(CONF_SIREN)): _entity(),
        vol.Optional(CONF_SIREN_DURATION,default=d.get(CONF_SIREN_DURATION,DEFAULT_SIREN_DURATION)): selector.NumberSelector(selector.NumberSelectorConfig(min=1,max=300,step=1,mode=selector.NumberSelectorMode.BOX)),
        vol.Optional(CONF_CRITICAL_ENTITIES,default=d.get(CONF_CRITICAL_ENTITIES,[])): _entity(multiple=True),
        vol.Optional(CONF_RF_ENTITIES,default=d.get(CONF_RF_ENTITIES,[])): _entity(multiple=True),
    })
class AlarmManagerConfigFlow(config_entries.ConfigFlow,domain=DOMAIN):
    VERSION=2
    async def async_step_user(self,user_input=None):
        if self._async_current_entries(): return self.async_abort(reason="single_instance_allowed")
        if user_input is not None: return self.async_create_entry(title=user_input.get(CONF_NAME) or DEFAULT_NAME,data=user_input)
        return self.async_show_form(step_id="user",data_schema=_schema({}))
    @staticmethod
    @callback
    def async_get_options_flow(config_entry): return AlarmManagerOptionsFlow()
class AlarmManagerOptionsFlow(config_entries.OptionsFlow):
    async def async_step_init(self,user_input=None):
        if user_input is not None: return self.async_create_entry(title="",data=user_input)
        return self.async_show_form(step_id="init",data_schema=_schema({**self.config_entry.data,**self.config_entry.options}))
