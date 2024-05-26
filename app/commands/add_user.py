from dependency_injector.wiring import Provide, inject
from loguru import logger
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from app.container import Container
from app.models import User


@inject
async def add_user(engine: Engine = Provide[Container.engine]):
    with Session(engine) as session:
        user = User(name="Test")
        session.add(user)
        session.commit()

    logger.debug(f"Created a user named 'Test'.")
