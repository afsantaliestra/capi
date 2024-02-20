"""src/gateway/exceptions.py - Exceptions"""
from typing import Any, Dict

from fastapi import HTTPException, status


class CustomHTTPException(HTTPException):
    """Custom HTTP Exception"""

    status_code: int
    detail: Any

    def __init__(
        self,
        status_code: int | None = None,
        detail: Any = None,
        headers: Dict[str, str] | None = None,
    ) -> None:
        super().__init__(status_code or self.status_code, detail or self.detail, headers)


class NotFoundHTTPException(CustomHTTPException):
    """Not Found HTTP Exception"""

    status_code: int = status.HTTP_404_NOT_FOUND
    detail: Any = "Not Found"


class ConflictHTTPException(CustomHTTPException):
    """Conflict HTTP Exception"""

    status_code: int = status.HTTP_409_CONFLICT
    detail: Any = "Conflict"


class DuplicatedHTTPException(ConflictHTTPException):
    """Duplicated HTTP Exception"""

    detail = "Duplicated"

    def __init__(
        self,
        status_code: int | None = None,
        detail: Any = None,
        headers: Dict[str, str] | None = None,
        extra_detail: str | None = None,
    ) -> None:
        if not detail and extra_detail:
            detail = f"{self.detail}: {extra_detail}"

        super().__init__(status_code or self.status_code, detail or self.detail, headers)
