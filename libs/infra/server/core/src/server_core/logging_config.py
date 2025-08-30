from . import EnvService
from server_core.logging_service import get_log_formater


def get_startup_logging_config(env_service: EnvService) -> dict:
  return {
  "version": 1,
  "disable_existing_loggers": False,
  "formatters": {
    "json": {
      "()": get_log_formater(env_service)
    }
  },
  "handlers": {
    "default": {
      "formatter": "json",
      "class": "logging.StreamHandler",
      "stream": "ext://sys.stdout",
    }
  },
  "loggers": {
    "uvicorn.access": {
      "handlers": ["default"],
      "level": "INFO",
      "propagate": False,
    },
    "uvicorn.error": {
      "handlers": ["default"],
      "level": "INFO",
      "propagate": False,
    },
    "openinference": {
      "handlers": ["default"],
      "level": "DEBUG",
      "propagate": False,
    },
    "google_adk": {
      "handlers": ["default"],
      "level": "DEBUG",
      "propagate": False,
    },
    "google_adk.google.adk.models.google_llm": {
      "handlers": ["default"],
      "level": "INFO",
      "propagate": False,
    },
  },
}
