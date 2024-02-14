"""src/__init__.py - API Configuration"""
from fastapi import FastAPI

from src.utils.lifespan import lifespan
from src.gateway.api import connectivity, users
from src.gateway.middlewares import LoggingMiddleware, RequestIdMiddleware

app = FastAPI(
    title="FastAPI - Character API",
    lifespan=lifespan,
)
app.include_router(connectivity.router)
app.include_router(users.router)

app.add_middleware(LoggingMiddleware)
app.add_middleware(RequestIdMiddleware)
