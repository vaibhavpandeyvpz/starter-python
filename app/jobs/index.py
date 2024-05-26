from dependency_injector.wiring import Provide, inject
from loguru import logger
from typing import Any, Dict

from app.container import Container


@inject
async def index(config: Dict[str, Any] = Provide[Container.config]):
    logger.debug(f"Running in '{config['app']['env']}' env.")
