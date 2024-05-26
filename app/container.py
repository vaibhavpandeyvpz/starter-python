from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Callable, Configuration, Singleton
from os import path
from redis import Redis
from rq import Queue
from sqlalchemy import create_engine


class Container(DeclarativeContainer):
    config = Configuration(
        ini_files=[
            path.join(path.dirname(__file__), "..", "config.ini"),
        ]
    )

    wiring_config = WiringConfiguration(
        modules=[
            ".commands",
            ".jobs",
            ".routers",
        ],
    )

    engine = Singleton(
        Callable(
            create_engine,
            config.db.url,
        )
    )

    redis = Singleton(
        Redis,
        host=config.redis.host,
        port=config.redis.port,
    )

    queue = Singleton(
        Queue,
        connection=redis,
    )
