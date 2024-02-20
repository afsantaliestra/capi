"""src/gateway/api/playground.py - Playground Routes"""
from beanie import PydanticObjectId
from fastapi import APIRouter, status

from src.gateway import exceptions
from src.gateway.schemas.accounts import AccountResponse, PostAccount
from src.infrastructure.account import Account
from src.infrastructure.user import User

router = APIRouter(prefix="/users", tags=["Accounts"])


@router.post(
    "/{user_id}/accounts",
    status_code=status.HTTP_201_CREATED,
    response_model=AccountResponse,
)
async def post_account(user_id: PydanticObjectId, account: PostAccount):
    """
    Post Account to a User
    """
    if not await User.get(user_id):
        raise exceptions.NotFoundHTTPException(detail="User Not Found")

    if await Account.find(Account.name == account.name, Account.user.id == user_id).count():
        raise exceptions.DuplicatedHTTPException()

    db_account = Account.from_api_object(account, user=await User.get(user_id))
    await db_account.insert()
    return db_account


@router.get(
    "/{user_id}/accounts",
    status_code=status.HTTP_200_OK,
)
async def get_accounts_by_user_id(user_id: PydanticObjectId):
    """
    Get Accounts by User If
    """
    if not await User.get(user_id):
        raise exceptions.NotFoundHTTPException(detail="User Not Found")

    accounts = await Account.find(Account.user.id == user_id).to_list()
    return accounts
