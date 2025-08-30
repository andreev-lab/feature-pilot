import json

import reactivex as rx
import reactivex.operators as ops
from fastapi import Depends, HTTPException
from pydantic import RootModel
from server_core import (
  EnvService,
  HttpClientService,
  LoggingService,
  inject_env_service,
  inject_http_client_service,
  inject_logger,
  map_root_model,
)

from git_server.data.git_repo_res import GitRepoRes


class GithubSdk:
  def __init__(
    self,
    http_client_service: HttpClientService = Depends(inject_http_client_service),
    logger: LoggingService = Depends(inject_logger),
    env_service: EnvService = Depends(inject_env_service),
  ):
    self.__http_client_service = http_client_service
    self.__logger = logger
    self.__env_service = env_service
    self.__oauth_access_token: str | None = None

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
      self.__oauth_access_token = response_data["access_token"]
    else:
      raise HTTPException(status_code=400, detail="Failed to obtain access token")

  def list_repos(self, org: str) -> rx.Observable[list[str]]:
    if not self.__oauth_access_token:
      raise HTTPException(
        status_code=401, detail="Not authenticated with GitHub."
      )
    self.__logger.info("here")
    headers = {
      "Authorization": f"Bearer {self.__oauth_access_token}",
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

  def auth_state(self):
    return {"is_authenticated": self.__oauth_access_token is not None}
