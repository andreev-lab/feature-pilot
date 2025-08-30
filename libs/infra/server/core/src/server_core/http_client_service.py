from functools import lru_cache
from typing import Dict, Any, Optional, TypeVar, Type, Union

import httpx
import reactivex as rx
from fastapi import Depends
from pydantic import BaseModel, RootModel
from reactivex.scheduler import ThreadPoolScheduler

from . import LoggingService, inject_logger

T = TypeVar("T", bound=Union[BaseModel, RootModel])

class HttpClientService:
  def __init__(self, logger: LoggingService):
    self._logger = logger
    self._client = httpx.Client(timeout=30.0)
    self._scheduler = ThreadPoolScheduler(max_workers=10)

  @staticmethod
  def __parse_response(json_response: Any, response_model: Optional[BaseModel]) -> Any:
    if response_model:
      return response_model.model_validate(json_response)
    return json_response

  def __handle_http_error(self, e: httpx.HTTPError):
    if e.response:
      msg = ""
      try:
        msg = e.response.json().get("message", e.response.text)
      except Exception:
        msg = e.response.text
      self._logger.error(f"""HTTP request failed: [{e.request.method}] {e.request.url} with {e.response.status_code}.
{msg}
""")
    else:
      self._logger.error(f"""HTTP request failed without a response: [{e.request.method}] {e.request.url}.
{e}
""")
    raise

  def get(
      self,
      url: str,
      params: Optional[Dict[str, Any]] = None,
      headers: Optional[Dict[str, str]] = None,
      response_model: Optional[Type[T]] = None
  ) -> rx.Observable[T]:
    def _make_request():
      try:
        self._logger.info(f"Making GET request to: {url}")
        response = self._client.get(url, params=params, headers=headers)
        response.raise_for_status()
        json_response = response.json()
        return self.__parse_response(json_response, response_model)
      except httpx.HTTPError as e:
        self.__handle_http_error(e)
      except Exception as e:
        self._logger.error(f"Unexpected error during HTTP request: {str(e)}")
        raise

    return rx.from_callable(_make_request, scheduler=self._scheduler)

  def post(self, url: str, body: Dict[str, Any], params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, response_model: Optional[Type[T]] = None) -> rx.Observable[T]:
    def _make_request():
      try:
        self._logger.info(f"Making POST request to: {url}")
        response = self._client.post(url, json=body, params=params, headers=headers)
        response.raise_for_status()
        json_response = response.json()
        return self.__parse_response(json_response, response_model)
      except httpx.HTTPError as e:
        self.__handle_http_error(e)
      except Exception as e:
        self._logger.error(f"Unexpected error during HTTP request: {str(e)}")
        raise

    return rx.from_callable(_make_request, scheduler=self._scheduler)


  def close(self):
    self._client.close()


@lru_cache
def inject_http_client_service(
  logger: LoggingService = Depends(inject_logger)
) -> HttpClientService:
  return HttpClientService(logger)


__all__ = ["inject_http_client_service", "HttpClientService"]
