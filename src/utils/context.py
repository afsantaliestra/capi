"""src/utils/context.py - Context variables"""
import contextvars

global_request_context: contextvars.ContextVar = contextvars.ContextVar(
    "global_request_context",
    default={},
)
