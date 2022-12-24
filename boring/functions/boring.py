from ..models import SshEndpoint


class BoringFunction:
    endpoint: SshEndpoint

    def __init__(self, endpoint: SshEndpoint):
        self.endpoint = endpoint

    def __call__(self):
        if self.endpoint.localhost:
            return self.handle_local()

        return self.handle_ssh()

    async def handle_local(self):
        raise NotImplementedError

    async def handle_ssh(self):
        raise NotImplementedError
