import asyncssh

from ..models import SshConnectionDetails
from .boring import BoringFunction
from .decorators import want_connection_details


class ConnectSsh(BoringFunction):
    async def handle_local(self):
        pass

    @want_connection_details
    async def handle_ssh(self, conn_details: SshConnectionDetails):
        options = {
            'known_hosts': None,
            'username': conn_details.username,
        }
        if conn_details.password is not None:
            options['password'] = conn_details.password
        if conn_details.client_key_path is not None:
            if not conn_details.client_key_path.is_file():
                raise ValueError(f'Client key file does not exist')
            options['client_keys'] = [conn_details.client_key_path.read_bytes()]

        conn_details._client_connection = await asyncssh.connect(
            conn_details.host,
            conn_details.port,
            **options,
        )
        return conn_details._client_connection
