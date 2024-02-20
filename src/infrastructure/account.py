"""src/infrastructure/accounts.py - Accounts"""
from beanie import Link
from pydantic import Field

from src.infrastructure import BaseDocument
from src.infrastructure.user import User


class Account(BaseDocument):
    """User"""

    name: str = Field(...)
    user: Link[User] = Field(...)

    class Settings:
        """Account Settings"""

        name = "accounts"
