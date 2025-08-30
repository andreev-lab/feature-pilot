from pydantic import BaseModel


class GitRepoRes(BaseModel):
  name: str
  url: str
