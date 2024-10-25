import logging  # noqa: D100

import aiohttp

LOGGER = logging.getLogger(__name__)


class NexusInstance:
    """Represents an instance of Nexus."""

    def __init__(self, ip_address: str) -> None:
        """Initialize the Nexus object.

        Args:
            ip_address (str): The IP address of the Nexus.

        Returns:
            None

        """

        self._ip_address = ip_address
        self._is_on = None
        self._connected = None

    @property
    def ip_address(self):
        """Returns the IP address of the Nexus object."""

        return self._ip_address

    @property
    def is_on(self):
        """Returns the current state of the object."""

        return self._is_on

    async def turn_on(self):
        """Turn on the device.

        Send a POST request to the device's LED endpoint to turn it on.
        If the request is successful (status code 200), update the device's state to 'on'.
        Otherwise, log an error message.
        """

        async with (
            aiohttp.ClientSession() as session,
            session.post(f"http://{self._ip_address}/led") as response,
        ):
            if response.status == 200:
                self._is_on = True
            else:
                LOGGER.error("Failed to turn on the device")

    async def turn_off(self):
        """Turn off the device.

        Send a POST request to the device's LED endpoint to turn it off.
        If the request is successful (status code 200), update the device's state to 'off'.
        Otherwise, log an error message.
        """
        async with (
            aiohttp.ClientSession() as session,
            session.post(f"http://{self._ip_address}/led") as response,
        ):
            if response.status == 200:
                self._is_on = False
            else:
                LOGGER.error("Failed to turn off the device")
