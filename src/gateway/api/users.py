"""src/gateway/api/connectivity.py - User Routes"""
from typing import Any

from fastapi import APIRouter

from src.fake_db import db  # TODO: Implement a real DB.
from src.gateway.schemas.users import UserResponseSchema, UsersResponseSchema

router = APIRouter(prefix="/users", tags=["Users"])


@router.get(
    "/",
    response_model=UsersResponseSchema,
)
def get_all_users() -> Any:
    """Get All Users"""
    return {
        "users": db["users"].values(),
        "count": len(db["users"]),
    }


@router.get(
    "/{code}",
    response_model=UserResponseSchema,
)
def get_user(code: int) -> Any:
    """Get User"""
    return db["users"][code]


@router.get(
    "/{code}/characters",
    # response_model=UserResponseSchema,
)
def get_user_characters(code: int) -> Any:
    """Get User"""
    characters = [character for character in db["characters"].values() if character["user_code"] == code]
    return characters
