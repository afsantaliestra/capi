"""src/infrastructure/accounts.py - Accounts"""
from beanie import Document, Link
from pydantic import Field

from src.infrastructure.user import User


class Account(Document):
    """User"""

    name: str = Field(...)
    user: Link[User] = Field(...)

    class Settings:
        """Account Settings"""

        name = "accounts"
