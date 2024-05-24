import asyncio

from app.commands import index as index_command
from app.container import Container

container = Container()


def index():
    asyncio.run(index_command())
