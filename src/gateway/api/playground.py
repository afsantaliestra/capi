"""src/gateway/api/playground.py - Playground Routes"""
from contextlib import suppress

from fastapi import APIRouter
from pymongo.errors import DuplicateKeyError

from src.infrastructure.account import Account
from src.infrastructure.character import Character
from src.infrastructure.rooster import Rooster
from src.infrastructure.server import Server
from src.infrastructure.tasks import CharacterTask, RoosterTask, Task
from src.infrastructure.user import User

router = APIRouter(tags=["Playground"])


@router.get(
    "/playground",
    status_code=200,
)
async def playground():
    """Playground"""
    with suppress(DuplicateKeyError):
        user = User(username="Necros")
        account = Account(name="Main", user=user)
        account_2 = Account(name="Seconday", user=user)
        server = Server(name="Thirain", region="EUC")
        server_2 = Server(name="Kayangel", region="EUC")
        rooster = Rooster(server=server, account=account, tasks=[])

        await user.insert()
        await account.insert()
        await account_2.insert()
        await server.insert()
        await server_2.insert()
        await rooster.insert()
        await rooster.sync()

        character = Character(name="Kay", user=user, account=account, rooster=rooster, tasks=[])
        await character.insert()
        await character.sync()

    rooster_tasks = [
        RoosterTask(
            name="Akkan G1-G3", frequency="weekly", repetitions=3, value=0, rooster=rooster
        ),
        RoosterTask(
            name="Brel G1-G3", frequency="weekly", repetitions=3, value=0, rooster=rooster
        ),
    ]
    character_tasks = [
        CharacterTask(
            name="Guardian Raid",
            frequency="daily",
            repetitions=1,
            value=0,
            character=character,
            min_ilvl=0,
            max_ilvl=9999,
        ),
        CharacterTask(
            name="Chaos Dungeon (x2)",
            frequency="daily",
            repetitions=2,
            value=0,
            character=character,
            min_ilvl=0,
            max_ilvl=9999,
        ),
    ]
    print("#######################################asd", rooster)
    for ctask in character_tasks:
        await ctask.insert()
    for rtask in rooster_tasks:
        await rtask.insert()

    print(
        "###############################################################################################asd"
    )
    rooster.tasks = rooster_tasks
    await rooster.save()
    character.tasks = character_tasks
    await character.save()

    return {"ok": "ok"}
