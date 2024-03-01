"""src/utils/lifespan.py - Lifespan"""
import asyncio
import logging
import typing
from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI
from mkdocs.commands import serve
from motor.core import AgnosticClient
from motor.motor_asyncio import AsyncIOMotorClient

from src.infrastructure.account import Account
from src.infrastructure.character import Character
from src.infrastructure.rooster import Rooster
from src.infrastructure.server import Server
from src.infrastructure.tasks import CharacterTask, RoosterTask, Task
from src.infrastructure.user import User
from src.utils.development import fill_db

logger = logging.getLogger()


async def initialize_beanie() -> None:
    """Initialize Beanie"""
    client: AgnosticClient = AsyncIOMotorClient("mongodb://localhost:27017/capi")
    await init_beanie(
        database=client.capi,
        document_models=[
            User,
            Account,
            Rooster,
            Server,
            Task,
            CharacterTask,
            RoosterTask,
            Character,
        ],
    )
    logger.debug(
        "Beanie Initialized",
        extra={
            "type": "api-startup",
        },
    )


async def launch_docs() -> None:
    """Launch Docs"""

    print("sirvo")
    serve.serve("./doc/mkdocs.yml")
    print("dejo de hacerlo")


@asynccontextmanager
async def lifespan(app: FastAPI) -> typing.AsyncGenerator:  # pylint: disable=unused-argument
    """Lifespan"""
    # On Startup
    logger.info(
        "Application Startup",
        extra={
            "type": "api-startup",
        },
    )

    await initialize_beanie()
    await fill_db()

    yield

    # On Shutdown
    logger.info(
        "Application Shutdown",
        extra={
            "type": "api-shutdown",
        },
    )
