"""src/infrastructure/tasks.py - Tasks"""
from typing import List

from beanie import Document, Link
from pydantic import Field

from src.infrastructure.account import Account
from src.infrastructure.server import Server
from src.infrastructure.tasks import RoosterTask


class Rooster(Document):
    """Rooster"""

    server: Link[Server] = Field(...)
    account: Link[Account] = Field(...)

    tasks: List[Link[RoosterTask]] = Field(None)
