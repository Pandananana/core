"""Platform for light integration."""

from __future__ import annotations

import logging
from pprint import pformat
from typing import Any

from homeassistant.components.light import LightEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS, CONF_NAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .nexus import NexusInstance

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Nexus Light config entry."""
    name = config_entry.data.get(CONF_NAME, "Nexus Light")
    light = {
        "name": name,
        "ip_address": config_entry.data[CONF_IP_ADDRESS],
    }
    async_add_entities([NexusLight(light)])


class NexusLight(LightEntity):
    """Representation of an Nexus Light."""

    def __init__(self, light) -> None:
        """Initialize an NexusLight."""
        _LOGGER.info(pformat(light))
        self._light = NexusInstance(light["ip_address"])
        self._name = light["name"]
        self._state = None

    @property
    def name(self) -> str:
        """Return the display name of this light."""
        return self._name

    @property
    def is_on(self) -> bool | None:
        """Return true if light is on."""
        return self._state

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Instruct the light to turn on."""
        await self._light.turn_on()

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Instruct the light to turn off."""
        await self._light.turn_off()

    def update(self) -> None:
        """Fetch new state data for this light."""
        self._state = self._light.is_on
