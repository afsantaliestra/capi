"""src/infrastructure/tasks.py - Tasks"""
from typing import List

from beanie import Document, Link
from pydantic import Field

from src.infrastructure.account import Account
from src.infrastructure.rooster import Rooster
from src.infrastructure.tasks import CharacterTask
from src.infrastructure.user import User


class Character(Document):
    """Character"""

    name: str = Field(...)

    user: Link[User] = Field(...)
    account: Link[Account] = Field(...)
    rooster: Link[Rooster] = Field(...)

    tasks: List[Link[CharacterTask]] = Field(...)
