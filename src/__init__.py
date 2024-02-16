"""src/__init__.py - API Configuration"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.gateway.api import checklist, connectivity, crud
from src.gateway.middlewares import LoggingMiddleware, RequestIdMiddleware
from src.utils.lifespan import lifespan

app = FastAPI(
    title="FastAPI - Character API",
    lifespan=lifespan,
)
app.include_router(connectivity.router)
app.include_router(crud.router)
app.include_router(checklist.router)

app.add_middleware(LoggingMiddleware)
app.add_middleware(RequestIdMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
