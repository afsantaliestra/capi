"""src/utils/development.py - Development"""
import logging

from src.infrastructure.account import Account
from src.infrastructure.character import Character
from src.infrastructure.rooster import Rooster
from src.infrastructure.server import Server
from src.infrastructure.tasks import Task
from src.infrastructure.user import User

logger = logging.getLogger()


async def clear_db() -> None:
    """Clear db"""
    await User.find_all().delete()
    await Account.find_all().delete()
    await Rooster.find_all().delete()
    await Server.find_all().delete()
    await Task.find_all().delete()
    await Character.find_all().delete()

    logger.info(
        "DB Cleared",
        extra={
            "type": "api-startup",
        },
    )


async def fill_db() -> None:
    """Fill db"""
    if await User.find_all().count():
        logger.debug(
            "DB Already Filled",
            extra={
                "type": "api-startup",
            },
        )
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
    logger.debug(
        "DB Filled",
        extra={
            "type": "api-startup",
        },
    )
