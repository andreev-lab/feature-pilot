import json
from functools import lru_cache

import reactivex as rx
import reactivex.operators as ops
from fastapi import Depends, HTTPException
from pydantic import RootModel
from server_core import (
  EnvService,
  HttpClientService,
  inject_env_service,
  inject_http_client_service,
  map_root_model,
  LoggingService,
  inject_logger,
)

from .git_db_service import inject_git_db_service, GitDbService
from .data.git_repo_res import GitRepoRes


class GithubSdk:
  def __init__(
    self,
    http_client_service: HttpClientService,
    logger: LoggingService,
    env_service: EnvService,
    git_db_service: GitDbService,
  ):
    self.__http_client_service = http_client_service
    self.__logger = logger
    self.__env_service = env_service
    self.__git_db_service = git_db_service

  def __get_token(self):
    token_data = self.__git_db_service.get_auth_token()
    if token_data and "token" in token_data:
      return token_data["token"]
    return None

  def get_github_auth_url(self) -> str:
    client_id = self.__env_service.git.github_client_id
    redirect_uri = f"{self.__env_service.server_url}/git/callback"
    scope = "repo"
    return (
      f"https://github.com/login/oauth/authorize?"
      f"client_id={client_id}&"
      f"redirect_uri={redirect_uri}&"
      f"scope={scope}"
    )

  async def handle_github_callback(self, code: str) -> None:
    client_id = self.__env_service.git.github_client_id
    client_secret = self.__env_service.git.github_client_secret
    redirect_uri = f"{self.__env_service.server_url}/git/callback"

    token_url = "https://github.com/login/oauth/access_token"
    headers = {"Accept": "application/json"}
    data = {
      "client_id": client_id,
      "client_secret": client_secret,
      "code": code,
      "redirect_uri": redirect_uri,
    }

    response_observable = self.__http_client_service.post(
      token_url, headers=headers, body=data
    )
    response_data = await response_observable.pipe(ops.to_future())

    if "access_token" in response_data:
      self.__logger.info(json.dumps(response_data))
      oauth_access_token = response_data["access_token"]
      self.__git_db_service.save_auth_token(oauth_access_token, "github")
    else:
      raise HTTPException(status_code=400, detail="Failed to obtain access token")

  def list_repos(self, org: str) -> rx.Observable[list[str]]:
    token = self.__get_token()
    if not token:
      raise HTTPException(
        status_code=401, detail="Not authenticated with GitHub."
      )
    self.__logger.info("here")
    headers = {
      "Authorization": f"Bearer {token}",
      "Accept": "application/vnd.github+json",
      "X-GitHub-Api-Version": "2022-11-28",
    }
    url = f"https://api.github.com/orgs/{org}/repos"

    return self.__http_client_service.get(
      url, headers=headers, response_model=RootModel[list[GitRepoRes]]
    ).pipe(
      ops.do_action(lambda r: self.__logger.info(r)),
      ops.map(map_root_model),
      ops.do_action(lambda r: self.__logger.info(r)),
    )

  def check_auth_status(self) -> rx.Observable[any]:
    token = self.__get_token()
    if not token:
      raise HTTPException(
        status_code=401, detail="Not authenticated with GitHub."
      )
    headers = {
      "Authorization": f"Bearer {token}",
      "Accept": "application/vnd.github+json",
      "X-GitHub-Api-Version": "2022-11-28",
    }
    url = "https://api.github.com/"

    return self.__http_client_service.get(url, headers=headers)

  def auth_state(self) -> rx.Observable[dict[str, bool]]:
    return self.check_auth_status().pipe(
      ops.map(lambda r: {"is_authenticated": r is not None}),
      ops.catch(
        rx.just({"is_authenticated": False})
      ),
    )


@lru_cache
def inject_github_sdk(
  http_client_service: HttpClientService = Depends(inject_http_client_service),
  logger: LoggingService = Depends(inject_logger),
  env_service: EnvService = Depends(inject_env_service),
  git_db_service: GitDbService = Depends(inject_git_db_service),
) -> GithubSdk:
  return GithubSdk(
    http_client_service=http_client_service,
    logger=logger,
    env_service=env_service,
    git_db_service=git_db_service,
  )
