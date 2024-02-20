"""src/gateway/middlewares.py - Global API Middlewares"""
import logging
import time
from uuid import uuid4

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.types import ASGIApp

from src.utils.context import global_request_context


class RequestIdMiddleware(BaseHTTPMiddleware):
    """Request Id Middleware"""

    def __init__(self, app: ASGIApp) -> None:
        """Init"""
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        """Dispatch"""
        start_time = time.time()
        request_id = request.headers.get("X-Request-Id", uuid4().hex)
        global_request_context.set({"request_id": request_id})

        response: Response = await call_next(request)

        response.headers["X-Process-Time"] = str(time.time() - start_time)
        response.headers["X-Request-Id"] = request_id

        return response


class LoggingMiddleware(BaseHTTPMiddleware):
    """Logging Middleware"""

    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)
        self.logger = logging.getLogger()

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        """Dispatch"""
        request_id = global_request_context.get().get("request_id")
        self.logger.info(
            "Request",
            extra={
                "request_id": request_id,
                "type": "api-request",
                "method": str(request.method).upper(),
                "url": str(request.url),
            },
        )

        response: Response = await call_next(request)

        self.logger.info(
            "Response sent",
            extra={
                "request_id": request_id,
                "type": "api-response",
                "code": response.status_code,
            },
        )

        return response
