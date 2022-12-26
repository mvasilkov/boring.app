from asyncssh.connection import SSHClientConnection
from pydantic import BaseModel


class SshConnectionDetails(BaseModel):
    host: str
    port: int = 22
    username: str
    password: str | None = None
    _client_connection: SSHClientConnection | None = None


class SshEndpoint(BaseModel):
    title: str
    # Connection details
    connection_details: SshConnectionDetails | None = None
    localhost: bool = False
    # Acquired properties
    hostname: str | None = None
