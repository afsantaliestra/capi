"""src/gateway/api/__init__.py - Gateway API"""
from fastapi import APIRouter

from src.gateway.api import users

api_router: APIRouter = APIRouter()
api_router.include_router(users.router)
