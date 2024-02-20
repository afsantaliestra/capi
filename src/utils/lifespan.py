"""src/utils/lifespan.py - Lifespan"""
import typing
from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from src.infrastructure.account import Account
from src.infrastructure.character import Character
from src.infrastructure.rooster import Rooster
from src.infrastructure.server import Server
from src.infrastructure.tasks import CharacterTask, RoosterTask, Task
from src.infrastructure.user import User


async def initialize_beanie() -> None:
    """Initialize Beanie"""
    client = AsyncIOMotorClient("mongodb://localhost:27017/capi")
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


@asynccontextmanager
async def lifespan(app: FastAPI) -> typing.AsyncGenerator:  # pylint: disable=unused-argument
    """Lifespan"""
    # On Startup
    print("Application Startup")
    await initialize_beanie()

    yield

    # On Shutdown
    print("Application Shutdown")
