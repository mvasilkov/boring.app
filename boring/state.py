from pydantic import BaseModel

from .models import SshConnectionDetails, SshEndpoint


class State(BaseModel):
    endpoints: list[SshEndpoint] = []
    connections: list[SshConnectionDetails] = []


def initialize_state():
    state = State(endpoints=[SshEndpoint(title='localhost', localhost=True)])
    return state


app_state = initialize_state()
