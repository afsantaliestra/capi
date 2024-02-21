"""src/gateway/api/connectivity.py - Connectivity Routes"""
from fastapi import APIRouter, Depends
from typing_extensions import Annotated

router = APIRouter()


async def cuak_from_function():
    print("CUAK FUNC")
    return "cauk"


async def cuak_from_path():
    print("CUAK PATH")


@router.get(
    "/playground",
    dependencies=[Depends(cuak_from_path)],
)
async def heartbeat(data: Annotated[dict, Depends(cuak_from_function)]):
    """ASD"""
    return {"me": data}
