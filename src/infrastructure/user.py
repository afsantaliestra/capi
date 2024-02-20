"""src/infrastructure/users.py - Users"""
from beanie import Document, Indexed
from pydantic import Field

from src.gateway.schemas.users import PostUser


class User(Document):
    """User"""

    username: Indexed(str, unique=True) = Field(...)

    @classmethod
    def from_user(cls, post_user: PostUser):
        """From PostUser Schema"""
        return cls(**post_user.model_dump())

    class Settings:
        """User Settings"""

        name = "users"
