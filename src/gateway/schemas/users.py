"""src/gateway/schemas/users.py - Users API schemas"""
from typing import List

from pydantic import BaseModel, Field


class UserResponseSchema(BaseModel):
    """User Response Schema"""

    code: int = Field(...)
    username: str = Field(...)
    display_name: str = Field(...)


class UsersResponseSchema(BaseModel):
    """Users Response Schema"""

    users: List[UserResponseSchema] = Field(...)
    count: int = Field(...)
