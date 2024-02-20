"""src/gateway/api/connectivity.py - Connectivity Routes"""
from fastapi import APIRouter
from starlette.responses import RedirectResponse

from src.gateway.schemas.connectivity import HeartbeatResponse
from src.infrastructure.account import Account
from src.infrastructure.character import Character
from src.infrastructure.rooster import Rooster
from src.infrastructure.server import Server
from src.infrastructure.tasks import Task
from src.infrastructure.user import User

router = APIRouter(tags=["Connectivity"])


@router.get(
    "/",
    include_in_schema=False,
)
def root_path() -> RedirectResponse:
    """Root path"""
    return RedirectResponse("/docs")


@router.get(
    "/heartbeat",
    status_code=200,
    response_model=HeartbeatResponse,
    responses={
        200: {
            "description": "Heartbeat response",
            "content": {"application/json": {"example": {"status": "ok"}}},
        },
    },
)
async def heartbeat(data: bool = False) -> HeartbeatResponse:
    """Heartbeat"""
    response_data = {
        table_obj.__name__: (
            {
                "data": db_data,
                "count": len(db_data),
            }
            if data
            else len(db_data)
        )
        for table_obj in [Server, Task, User, Account, Rooster, Character]
        if (db_data := await table_obj.find_all().to_list())
    }

    return HeartbeatResponse(status="ok", db_data=response_data)
