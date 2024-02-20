"""src/gateway/schemas/users.py - User Schemas"""
from pydantic import BaseModel, Field


class PostUser(BaseModel):
    """Post User"""

    username: str = Field(...)


class UserResponse(PostUser):
    """User Response"""
