"""src/utils/logging.py - Logging"""
import json
import logging
from datetime import datetime
from json import JSONEncoder
from logging.config import dictConfig
from uuid import UUID, uuid4

from pythonjsonlogger import jsonlogger


# Custom JSON encoder which enforce standard ISO 8601 format, UUID format
class ModelJsonEncoder(JSONEncoder):
    """Model Json Encoder"""

    def default(self, o):
        """Default"""
        if isinstance(o, UUID):
            return str(o)

        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)


class LogFilter(logging.Filter):
    """Log Filter"""

    def __init__(self, service=None, instance=None):
        """Init"""
        super().__init__()

        self.service = service
        self.instance = instance

    def filter(self, record):
        """Filter"""
        record.service = self.service
        record.instance = self.instance
        return True


class JsonLogFormatter(jsonlogger.JsonFormatter):
    """Json Log Formatter"""

    def add_fields(self, log_record, record, message_dict):
        """Add Fields"""
        super().add_fields(log_record, record, message_dict)

        # Add timestamp field with default: now
        if not log_record.get("timestamp"):
            now = datetime.utcnow().isoformat()
            log_record["timestamp"] = now

        # Add level field
        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname

        # Add type field for internal logs
        if not log_record.get("type"):
            log_record["type"] = "internal"


# Configure Logging
def configure_logging(level="DEBUG", service=None, instance=None):
    """Configure Logging"""
    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "()": JsonLogFormatter,
                    "format": " ".join(
                        [
                            "%(timestamp)s",
                            "%(level)s",
                            "%(service)s",
                            "%(instance)s",
                            "%(type)s",
                            "%(message)s",
                        ]
                    ),
                    "json_encoder": ModelJsonEncoder,
                }
            },
            "filters": {
                "default": {
                    "()": LogFilter,
                    "service": service,
                    "instance": instance or uuid4().hex,
                }
            },
            "handlers": {
                "default_handler": {
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                    "filters": ["default"],
                    "formatter": "default",
                }
            },
            "root": {
                "level": level,
                "handlers": ["default_handler"],
            },
        }
    )
