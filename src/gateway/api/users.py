"""src/gateway/api/connectivity.py - User Routes"""
from typing import Any
from uuid import uuid4

from aiotinydb import AIOTinyDB
from fastapi import APIRouter
from tinydb import Query
from tinydb.database import Table

from src.gateway.schemas.users import PostUserSchema, UserResponseSchema, UsersResponseSchema

router = APIRouter(prefix="/users", tags=["Users"])
tinydb: AIOTinyDB = AIOTinyDB("./local_dbs/tiny_db.json")


@router.post(
    "/",
)
async def post_user(user: PostUserSchema) -> Any:
    """Post User"""
    new_user = {**user.model_dump(), "code": uuid4().hex}

    async with tinydb as database:
        table: Table = database.table("users")

        # No other user with same username
        user = table.get(Query().username == new_user["username"])
        if user:
            return None  # TODO: Improve response to a 404.

        # Insert user
        table.insert(new_user)

    return new_user


@router.get(
    "/",
    response_model=UsersResponseSchema,
)
async def get_all_users() -> Any:
    """Get All Users"""
    async with tinydb as database:
        table: Table = database.table("users")
        users = table.all()

    return UsersResponseSchema(users=users, count=len(users))


@router.get(
    "/{code}",
    response_model=UserResponseSchema,
)
async def get_user(code: str) -> Any:
    """Get User"""
    async with tinydb as database:
        table: Table = database.table("users")
        user = table.get(Query().code == code)

    return UserResponseSchema(**user)
