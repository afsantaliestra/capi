"""src/infrastructure/users.py - Users"""
from beanie import Indexed
from pydantic import Field

from src.infrastructure import BaseDocument


class User(BaseDocument):
    """User"""

    username: Indexed(str, unique=True) = Field(...)

    class Settings:
        """User Settings"""

        name = "users"
