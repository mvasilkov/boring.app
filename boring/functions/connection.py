import asyncssh

from ..models import SshConnectionDetails
from .boring import BoringFunction
from .decorators import want_connection_details


class ConnectSsh(BoringFunction):
    async def handle_local(self):
        pass

    @want_connection_details
    async def handle_ssh(self, conn_details: SshConnectionDetails):
        conn_details.client_connection = await asyncssh.connect(
            conn_details.host,
            conn_details.port,
            known_hosts=None,
            username=conn_details.username,
            password=conn_details.password,
        )
        return conn_details.client_connection
