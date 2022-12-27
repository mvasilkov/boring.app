from pathlib import Path

from asyncssh.connection import SSHClientConnection
from nanoid import generate
from pydantic import BaseModel, Field


class SshConnectionDetails(BaseModel):
    host: str
    port: int = 22
    username: str
    password: str | None = None
    client_key_path: Path | None = None
    # Private attributes
    _client_key: bytes | None = None
    _client_connection: SSHClientConnection | None = None


class SshEndpoint(BaseModel):
    pk: str = Field(default_factory=generate)
    parent: str | None
    title: str
    # Connection details
    connection_details: SshConnectionDetails | None = None
    localhost: bool = False
    # Acquired properties
    hostname: str | None = None
