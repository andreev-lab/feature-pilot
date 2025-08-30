from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from .git_service import GitService, inject_git_service

git_router = APIRouter(prefix="/git")


class GitRequest(BaseModel):
  repo_url: str
  branch: str = 'main'


class ListReposRequest(BaseModel):
  org: str
  pat: str


@git_router.get("/login/github")
async def github_login(
  git_service: GitService = Depends(inject_git_service)
):
  return RedirectResponse(git_service.get_github_auth_url())


@git_router.get("/callback")
async def github_callback(
  code: str,
  git_service: GitService = Depends(inject_git_service)
):
  await git_service.handle_github_callback(code)
  return RedirectResponse(url="/")


@git_router.post("/clone")
def clone_repo(
  request: GitRequest, git_service: GitService = Depends(inject_git_service)
):
  try:
    return {"message": git_service.clone_repo(request.repo_url)}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e)) from e


@git_router.post("/readme")
def get_readme(
  request: GitRequest, git_service: GitService = Depends(inject_git_service)
):
  try:
    return {"readme": git_service.get_readme(request.repo_url)}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e)) from e


@git_router.post("/push")
def push_repo(
  request: GitRequest, git_service: GitService = Depends(inject_git_service)
):
  try:
    return {"message": git_service.push_repo(request.repo_url, request.branch)}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e)) from e


@git_router.post("/list-repos")
async def list_repos(
  request: ListReposRequest, git_service: GitService = Depends(inject_git_service)
):
  try:
    return {"repos": await git_service.list_repos(request.org)}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e)) from e


@git_router.get("/check-auth")
async def check_auth(git_service: GitService = Depends(inject_git_service)):
  return  git_service.auth_state()
