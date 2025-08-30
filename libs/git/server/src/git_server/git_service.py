from functools import lru_cache
from typing import Optional

from fastapi import Depends
from reactivex import operators
from server_core import (
  EnvService,
  HttpClientService,
  LoggingService,
  inject_env_service,
  inject_http_client_service,
  inject_logger,
)

from .data.git_repo_res import GitRepoRes
from .git_sdk import GitSdk
from .github_sdk import GithubSdk


class GitService:
  def __init__(
    self,
    http_client_service: HttpClientService = Depends(inject_http_client_service),
    logger: LoggingService = Depends(inject_logger),
    env_service: EnvService = Depends(inject_env_service),
    github_sdk: GithubSdk = Depends(GithubSdk),
  ):
    self.__http_client_service = http_client_service
    self.__logger = logger
    self.__env_service = env_service
    self.__github_sdk = github_sdk

  def __get_git_sdk(self, repo_url: Optional[str] = None) -> GitSdk:
    return GitSdk(
      repo_url=repo_url,
      http_client_service=self.__http_client_service,
      logger=self.__logger,
    )

  def get_github_auth_url(self) -> str:
    return self.__github_sdk.get_github_auth_url()

  async def handle_github_callback(self, code: str) -> None:
    await self.__github_sdk.handle_github_callback(code)

  def clone_repo(self, repo_url: str) -> str:
    sdk = self.__get_git_sdk(repo_url)
    return sdk.clone()

  def get_readme(self, repo_url: str) -> str:
    sdk = self.__get_git_sdk(repo_url)
    return sdk.get_readme()

  def push_repo(self, repo_url: str, branch: str) -> str:
    sdk = self.__get_git_sdk(repo_url)
    return sdk.push(branch)

  async def list_repos(self, org: str) -> list[GitRepoRes]:
    return await self.__github_sdk.list_repos(org).pipe(operators.to_future())

  def auth_state(self):
    return self.__github_sdk.auth_state()


@lru_cache
def inject_git_service(
  http_client_service: HttpClientService = Depends(inject_http_client_service),
  logger: LoggingService = Depends(inject_logger),
  env_service: EnvService = Depends(inject_env_service),
  github_sdk: GithubSdk = Depends(GithubSdk),
) -> GitService:
  return GitService(
    http_client_service=http_client_service,
    logger=logger,
    env_service=env_service,
    github_sdk=github_sdk,
  )
