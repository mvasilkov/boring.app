import socket

from asyncssh.connection import SSHClientConnection

from .boring import BoringFunction, coerce_string
from .decorators import want_client_connection


class GetHostname(BoringFunction):
    async def handle_local(self):
        self.endpoint.hostname = socket.gethostname()
        return self.endpoint.hostname

    @want_client_connection
    async def handle_ssh(self, client_conn: SSHClientConnection):
        result = await client_conn.run('hostname')
        self.endpoint.hostname = coerce_string(result.stdout)
        return self.endpoint.hostname
