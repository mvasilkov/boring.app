from fastapi import FastAPI
from pydantic import BaseModel


class SshConnectionDetails(BaseModel):
    host: str
    port: int
    username: str
    password: str


app = FastAPI()


@app.get('/')
async def index():
    return {}
