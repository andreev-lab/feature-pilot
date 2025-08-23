import os
from functools import lru_cache
from typing import Self, Literal

from dotenv import load_dotenv

load_dotenv()

ENV_TYPE_LIST = ["local", "dev", "prod"]
EnvType = Literal["local", "dev", "prod"]


class EnvService:

  @property
  @lru_cache()
  def port(self: Self) -> int:
    port_value = self.__get_env_var("PORT", required=True)
    assert port_value is not None
    try:
      return int(port_value)
    except ValueError:
      raise ValueError("PORT must be a valid integer")

  @property
  @lru_cache()
  def log_format(self: Self) -> str:
    log_format_value = self.__get_env_var("LOG_FORMAT", default="", required=False)
    assert log_format_value is not None
    return log_format_value

  @lru_cache()
  def env(self: Self) -> EnvType:
    env_value = self.__get_env_var("ENV", required=True)
    assert env_value is not None
    if env_value not in ENV_TYPE_LIST:
      raise ValueError("ENV must be one of the following: local, dev, prod")
    return env_value # type: ignore[return-value]

  @lru_cache()
  def is_local(self: Self) -> bool:
    return self.env() == "local"

  @staticmethod
  def __get_env_var(key: str, default: str | None = None, required: bool = True) -> str | None:
    value = os.getenv(key)
    if value is None:
      if required:
        raise ValueError(f"Environment variable '{key}' is not set and is required.")
      return default
    return value

@lru_cache()
def inject_env_service():
  return EnvService()


__all__ = ['EnvService', 'inject_env_service']
