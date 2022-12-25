from pydantic import BaseModel

from .models import SshEndpoint


class State(BaseModel):
    endpoints: list[SshEndpoint] = []


def initialize_state():
    state = State(endpoints=[SshEndpoint(title='localhost', localhost=True)])
    return state


app_state = initialize_state()
