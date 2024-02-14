"""src/utils/lifespan.py - Lifespan"""
import typing
from contextlib import asynccontextmanager

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI) -> typing.AsyncGenerator:  # pylint: disable=unused-argument
    """Lifespan"""
    # On Startup
    print("Application Startup")

    yield

    # On Shutdown
    print("Application Shutdown")
