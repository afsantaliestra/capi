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


async def clear_db() -> None:
    """Clear db"""
    await User.find_all().delete()
    await Account.find_all().delete()
    await Rooster.find_all().delete()
    await Server.find_all().delete()
    await Task.find_all().delete()
    await Character.find_all().delete()


async def fill_db() -> None:
    """Fill db"""
    if await User.find_all().count():
        return

    await clear_db()

    for username in ["Necros", "Sorcen"]:
        user = User(username=username)
        await user.insert()

        for account_name in ["Main", "Secondary"]:
            account = Account(name=f"{username} {account_name}", user=user)
            await account.insert()

            for server_name in ["Thirain", "Kayangel"]:
                server = Server(name=server_name, region="EUC")
                await server.insert()
                rooster = Rooster(server=server, account=account)
                await rooster.insert()

                for character in ["Slayer", "Sorceress"]:
                    character = Character(
                        name=f"{character}{account_name}{username}",
                        user=user,
                        account=account,
                        rooster=rooster,
                    )
                    await character.insert()


@asynccontextmanager
async def lifespan(app: FastAPI) -> typing.AsyncGenerator:  # pylint: disable=unused-argument
    """Lifespan"""
    # On Startup
    print("Application Startup")
    await initialize_beanie()
    await fill_db()

    yield

    # On Shutdown
    print("Application Shutdown")
