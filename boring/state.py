from pydantic import BaseModel

from .models import SshEndpoint


class State(BaseModel):
    endpoints: list[SshEndpoint] = []


def initialize_state() -> State:
    state = State(endpoints=[SshEndpoint(parent=None, title='localhost', localhost=True)])
    return state


def find_endpoint(pk: str) -> SshEndpoint | None:
    for endpoint in app_state.endpoints:
        if endpoint.pk == pk:
            return endpoint


app_state = initialize_state()
