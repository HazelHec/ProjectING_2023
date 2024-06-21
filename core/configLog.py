import logging
from logging.config import dictConfig

log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
        "access": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "formatter": "default",
            "filename": "server.log",
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "access_file": {
            "class": "logging.FileHandler",
            "formatter": "access",
            "filename": "access.log",
        },
        "access_console": {
            "class": "logging.StreamHandler",
            "formatter": "access",
        },
    },
    "loggers": {
        "uvicorn": {
            "handlers": ["file", "console"],
            "level": "INFO",
            "propagate": False,
        },
        "uvicorn.error": {
            "handlers": ["file", "console"],
            "level": "ERROR",
            "propagate": False,
        },
        "uvicorn.access": {
            "handlers": ["access_file", "access_console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

dictConfig(log_config)
