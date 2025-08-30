import os
import subprocess

from fastapi import Depends
from server_core import (
  HttpClientService,
  LoggingService,
  inject_http_client_service,
  inject_logger,
)


class GitSdk:
  def __init__(
    self,
    repo_url: str = None,
    base_dir: str = "/tmp/git_sdk_repos",
    http_client_service: HttpClientService = Depends(inject_http_client_service),
    logger: LoggingService = Depends(inject_logger),
  ):
    self.__repo_url = repo_url
    self.__base_dir = base_dir
    self.__http_client_service = http_client_service
    self.__logger = logger
    if repo_url:
      self.__repo_dir = os.path.join(
        self.__base_dir, self.__repo_url.split("/")[-1].replace(".git", "")
      )
      os.makedirs(self.__repo_dir, exist_ok=True)
      self.clone()

  def __run_command(self, command: list[str], cwd: str = None):
    try:
      result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        check=True,
        cwd=cwd or self.__repo_dir,
      )
      return result.stdout.strip()
    except subprocess.CalledProcessError as e:
      return f"Error: {e.stderr.strip()}"

  def clone(self):
    if os.path.exists(os.path.join(self.__repo_dir, ".git")):
      return "Repository already cloned."

    command = ["git", "clone", self.__repo_url, self.__repo_dir]
    return self.__run_command(command, cwd=self.__base_dir)

  def get_readme(self):
    readme_path = os.path.join(self.__repo_dir, "README.md")
    if not os.path.exists(readme_path):
      return "README.md not found."
    with open(readme_path) as f:
      return f.read()

  def push(self, branch: str = "main"):
    command = ["git", "push", "origin", branch]
    return self.__run_command(command)
