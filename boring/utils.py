from asyncio import AbstractEventLoop
from functools import partial
from typing import Callable, TypeVar

T = TypeVar('T')


async def run_in_executor(loop: AbstractEventLoop, function: Callable[..., T], *args, **kwargs) -> T:
    return await loop.run_in_executor(None, partial(function, *args, **kwargs))


def strip_trailing_newline(value: str):
    if value.endswith('\r\n'):
        return value[:-2]
    if value.endswith('\n'):
        return value[:-1]
    return value


def coerce_string(value, keep_trailing_newline=False):
    if isinstance(value, str):
        result = value
    elif isinstance(value, bytes):
        result = value.decode('utf-8')
    else:
        return None

    return result if keep_trailing_newline else strip_trailing_newline(result)
