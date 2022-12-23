from fastapi import FastAPI

from .state import State, app_state

app = FastAPI()


@app.on_event('startup')
async def startup():
    pass


@app.get('/', response_model=State)
async def index():
    return app_state
