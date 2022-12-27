import asyncssh

from ..models import SshConnectionDetails
from ..state import find_endpoint
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
        if conn_details._client_key is not None:
            options['client_keys'] = [conn_details._client_key]
        elif conn_details.client_key_path is not None:
            if not conn_details.client_key_path.is_file():
                raise ValueError('Client key file does not exist')
            conn_details._client_key = conn_details.client_key_path.read_bytes()
            options['client_keys'] = [conn_details._client_key]

        conn_details._client_connection = await asyncssh.connect(
            conn_details.host,
            conn_details.port,
            tunnel=await self.get_tunnel(),
            **options,
        )
        return conn_details._client_connection

    async def get_tunnel(self):
        if self.endpoint.parent is None:
            return None
        parent_endpoint = find_endpoint(self.endpoint.parent)
        if parent_endpoint is None:
            raise ValueError('Missing parent endpoint')
        connect_ssh = ConnectSsh(parent_endpoint)
        return await connect_ssh()
