import socket

from .boring import BoringFunction


class GetHostname(BoringFunction):
    async def handle_local(self):
        self.endpoint.hostname = socket.gethostname()
        return self.endpoint.hostname

    async def handle_ssh(self):
        pass
