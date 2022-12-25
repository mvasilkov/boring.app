import socket

from .boring import BoringFunction, coerce_string
from .connection import ConnectSsh


class GetHostname(BoringFunction):
    async def handle_local(self):
        self.endpoint.hostname = socket.gethostname()
        return self.endpoint.hostname

    async def handle_ssh(self):
        if (conn_details := self.endpoint.connection_details) is None:
            raise ValueError('Missing connection details')

        if (client_conn := conn_details.client_connection) is None:
            connect_ssh = ConnectSsh(self.endpoint)
            client_conn = await connect_ssh()

        result = await client_conn.run('hostname')
        self.endpoint.hostname = coerce_string(result.stdout)
        return self.endpoint.hostname
