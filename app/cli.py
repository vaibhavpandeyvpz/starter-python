import asyncio

from .commands import add_user as add_user_command
from .container import Container

container = Container()


def add_user():
    asyncio.run(add_user_command())
