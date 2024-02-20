"""src/infrastructure/users.py - Users"""
from beanie import Document, Indexed
from pydantic import Field


class User(Document):
    """User"""

    username: Indexed(str, unique=True) = Field(...)

    class Settings:
        """User Settings"""

        name = "users"
