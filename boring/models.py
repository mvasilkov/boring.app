from pydantic import BaseModel


class SshConnectionDetails(BaseModel):
    host: str
    port: int
    username: str
    password: str


class SshEndpoint(BaseModel):
    title: str
    connection: SshConnectionDetails | None = None
    localhost: bool = False
