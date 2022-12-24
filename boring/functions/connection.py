import asyncssh

from .boring import BoringFunction


class ConnectSsh(BoringFunction):
    async def handle_local(self):
        pass

    async def handle_ssh(self):
        if (conn_details := self.endpoint.connection_details) is None:
            raise ValueError('Missing connection details')

        conn_details.client_connection = await asyncssh.connect(
            conn_details.host,
            conn_details.port,
            username=conn_details.username,
            password=conn_details.password,
        )
        return conn_details.client_connection
