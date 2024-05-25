import asyncio

from .commands import index as index_command
from .container import Container

container = Container()


def index():
    asyncio.run(index_command())
