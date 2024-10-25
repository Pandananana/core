"""Config flow for Project Nexus integration."""

from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_IP_ADDRESS, CONF_NAME

_LOGGER = logging.getLogger(__name__)

DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_IP_ADDRESS): str,
        vol.Optional(CONF_NAME, default="Nexus Light"): str,
    }
)


class ProjectNexusConfigFlow(config_entries.ConfigFlow, domain="project_nexus"):
    """Handle a config flow for Project Nexus."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.ConfigFlowResult:
        """Handle the initial step."""
        if user_input is None:
            return self.async_show_form(
                step_id="user",
                data_schema=DATA_SCHEMA,
            )

        _LOGGER.debug("Config flow user input: %s", user_input)  # Debug log

        # Make sure the data is properly structured
        data = {
            CONF_IP_ADDRESS: user_input[CONF_IP_ADDRESS],
            CONF_NAME: user_input.get(CONF_NAME, "Nexus Light"),
        }

        _LOGGER.debug("Config entry data to be saved: %s", data)  # Debug log

        return self.async_create_entry(title=data[CONF_NAME], data=data)
