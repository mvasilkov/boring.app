from pydantic import BaseModel

from .models import SshEndpoint


class State(BaseModel):
    endpoints: list[SshEndpoint] = []


def initialize_state():
    state = State(endpoints=[SshEndpoint(parent=None, title='localhost', localhost=True)])
    return state


app_state = initialize_state()
