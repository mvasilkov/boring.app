from functools import wraps

from .boring import BoringFunction


def want_connection_details(function):
    @wraps(function)
    async def wrapper(self: BoringFunction):
        if (conn_details := self.endpoint.connection_details) is None:
            raise ValueError('Missing connection details')

        return await function(self, conn_details)

    return wrapper


def want_client_connection(function):
    @wraps(function)
    async def wrapper(self: BoringFunction):
        if (conn_details := self.endpoint.connection_details) is None:
            raise ValueError('Missing connection details')

        if (client_conn := conn_details.client_connection) is None:
            from .connection import ConnectSsh

            connect_ssh = ConnectSsh(self.endpoint)
            client_conn = await connect_ssh()

        return await function(self, client_conn)

    return wrapper
