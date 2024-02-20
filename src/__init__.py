"""src/__init__.py - API Configuration"""
import toml
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.gateway.api import api_router, connectivity
from src.gateway.middlewares import LoggingMiddleware, RequestIdMiddleware
from src.utils.lifespan import lifespan
from src.utils.logging import configure_logging

pyproject = toml.load("pyproject.toml")

TITLE = "FastAPI - CAPI"

configure_logging(level="DEBUG", service=TITLE)

app = FastAPI(
    title=TITLE,
    description=pyproject["tool"]["poetry"]["description"],
    version=pyproject["tool"]["poetry"]["version"],
    lifespan=lifespan,
)

app.include_router(connectivity.router)
app.include_router(api_router, prefix="/api")

app.add_middleware(LoggingMiddleware)
app.add_middleware(RequestIdMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
