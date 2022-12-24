from asyncssh.connection import SSHClientConnection
from pydantic import BaseModel


class SshConnectionDetails(BaseModel):
    host: str
    port: int = 22
    username: str
    password: str | None = None
    client_connection: SSHClientConnection | None = None

    class Config:
        arbitrary_types_allowed = True


class SshEndpoint(BaseModel):
    title: str
    # Connection details
    connection_details: SshConnectionDetails | None = None
    localhost: bool = False
    # Acquired properties
    hostname: str | None = None
