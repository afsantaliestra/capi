"""src/utils/context.py - Context variables"""
import contextvars
import types

global_request_context = contextvars.ContextVar(
    "global_request_context",
    default={},
)
