"""src/gateway/api/playground.py - Playground Routes"""
from beanie import PydanticObjectId
from fastapi import APIRouter, status

from src.gateway import exceptions
from src.gateway.schemas.users import PostUser, UserResponse
from src.infrastructure.user import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse,
)
async def post_user(user: PostUser):
    """
    Post User
    """
    if await User.find(User.username == user.username).count():
        raise exceptions.DuplicatedHTTPException()

    db_user = User.from_user(user)
    await db_user.insert()
    return db_user


@router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
)
async def get_user_by_id(user_id: PydanticObjectId):
    """
    Get User by Id
    """
    if not (user := await User.get(user_id)):
        raise exceptions.NotFoundHTTPException()

    return user


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
)
async def get_all_users():
    """
    Get All Users
    """
    return await User.find_all().to_list()


@router.put(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
)
async def update_user_by_id(user_id: PydanticObjectId, new_username: str):
    """
    Update User by Id
    """
    if not (user := await User.get(user_id)):
        raise exceptions.NotFoundHTTPException()

    user.username = new_username
    await user.save()
    return user


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user_by_id(user_id: PydanticObjectId):
    """
    Delete User by Id
    """
    if not (user := await User.get(user_id)):
        raise exceptions.NotFoundHTTPException()

    await user.delete()
    return user
