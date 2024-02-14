"""src/gateway/schemas/users.py - Users API schemas"""
from typing import List

from pydantic import BaseModel, Field


class PostUserSchema(BaseModel):
    """Post User Schema"""

    username: str = Field(...)
    display_name: str = Field(...)


class UserResponseSchema(BaseModel):
    """User Response Schema"""

    code: str = Field(...)
    username: str = Field(...)
    display_name: str = Field(...)


class UsersResponseSchema(BaseModel):
    """Users Response Schema"""

    count: int = Field(...)
    users: List[UserResponseSchema] = Field(...)
