"""src/gateway/api/connectivity.py - Connectivity Routes"""

from aiotinydb import AIOTinyDB
from fastapi import APIRouter
from starlette.responses import RedirectResponse

from src.gateway.schemas.connectivity import HeartbeatResponseSchema

router = APIRouter(tags=["Connectivity"])
tinydb: AIOTinyDB = AIOTinyDB("./local_dbs/tiny_db.json")


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
    response_model=HeartbeatResponseSchema,
    responses={
        200: {
            "description": "Heartbeat response",
            "content": {"application/json": {"example": {"status": "ok"}}},
        },
    },
)
async def heartbeat(data: bool = False) -> HeartbeatResponseSchema:
    """Heartbeat"""
    async with tinydb as database:
        response_data = {
            table: (
                {
                    "data": db_data,
                    "count": len(db_data),
                }
                if data
                else {
                    "count": len(db_data),
                }
            )
            for table in database.tables()
            if (db_data := database.table(table).all())
        }

    return HeartbeatResponseSchema(status="ok", db_data=response_data)
