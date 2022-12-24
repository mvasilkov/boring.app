import socket

from .boring import BoringFunction


class GetHostname(BoringFunction):
    async def handle_localhost(self):
        return socket.gethostname()

    async def handle_ssh(self):
        pass
