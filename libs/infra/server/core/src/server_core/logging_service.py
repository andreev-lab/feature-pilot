import logging
import os
import sys
from functools import lru_cache
from typing import Self, Optional

from fastapi.params import Depends

from .env_service import EnvService, inject_env_service
from .json_formater import JsonFormatter

COLORS = {
  'DEBUG': '\033[94m',  # Blue
  'INFO': '\033[92m',  # Green
  'WARNING': '\033[93m',  # Yellow
  'ERROR': '\033[38;5;174m',  # Much lighter red shade
  'CRITICAL': '\033[1;31m',  # Bold intense red
  'RESET': '\033[0m'  # Reset
}


class ColorFormatter(logging.Formatter):
  """A formatter that adds colors to logs in local environment"""

  def format(self, record):
    levelname = record.levelname
    message = super().format(record)
    if levelname in COLORS:
      return f"{COLORS[levelname]}{message}{COLORS['RESET']}"
    return message


def get_log_formater(env_service: EnvService):
  """
  this is used in the main.py and passed to the framework, so that all logs are using the same structure.
  We need to pass the class itself and not an instance so we do have a slight code duplication, but I can live with that.
  :param env_service:
  :return:
  """
  if env_service.is_local():
    return ColorFormatter
  else:
    return JsonFormatter


class LoggingService:
  def __init__(self: Self, env_service: EnvService) -> None:
    log_level_str = os.getenv("LOG_LEVEL", "INFO").upper()
    log_level = getattr(logging, log_level_str, logging.INFO)

    handler = logging.StreamHandler(sys.stdout)

    if env_service.is_local():
      handler.setFormatter(ColorFormatter(env_service.log_format))
    else:
      handler.setFormatter(JsonFormatter())

    self.logger = logging.getLogger("muninn")
    self.logger.setLevel(log_level)

    if self.logger.handlers:
      self.logger.handlers.clear()
    self.logger.addHandler(handler)
    self.logger.propagate = False

  def debug(self: Self, message: str, extra: Optional[dict] = None, exc_info=None) -> None:
    self.logger.debug(message, extra=extra, exc_info=exc_info)

  def info(self: Self, message: str, extra: Optional[dict] = None, exc_info=None) -> None:
    self.logger.info(message, extra=extra, exc_info=exc_info)

  def warning(self: Self, message: str, extra: Optional[dict] = None, exc_info=None) -> None:
    self.logger.warning(message, extra=extra, exc_info=exc_info)

  def error(self: Self, message: str, extra: Optional[dict] = None, exc_info=None) -> None:
    self.logger.error(message, extra=extra, exc_info=exc_info)

  def critical(self: Self, message: str, extra: Optional[dict] = None, exc_info=None) -> None:
    self.logger.critical(message, extra=extra, exc_info=exc_info)

  def exception(self, exc: Exception, message: Optional[str] = None) -> None:
    self.error(message or str(exc), exc_info=exc)

  def get_logger(self: Self, name: str) -> logging.Logger:
    return self.logger.getChild(name)


@lru_cache()
def inject_logger(
  env_service: EnvService = Depends(inject_env_service)
) -> LoggingService:
  """For use with FastAPI dependency injection"""
  return LoggingService(env_service)

__all__ = ['LoggingService', 'inject_logger']
