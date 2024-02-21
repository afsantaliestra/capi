"""src/gateway/api/__init__.py - Gateway API"""
from fastapi import APIRouter

from src.gateway.api import accounts, playground, users

api_router: APIRouter = APIRouter()
api_router.include_router(users.router)
api_router.include_router(accounts.router)
api_router.include_router(playground.router)
