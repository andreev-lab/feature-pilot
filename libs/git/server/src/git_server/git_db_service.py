from fastapi.params import Depends
from tinydb import TinyDB
from server_core import inject_db, DbQuery
from functools import lru_cache


class GitDbService:
  def __init__(self, db: TinyDB):
    self.__db = db

  def save_auth_token(self, token: str, origin: str):
    Token = DbQuery()
    self.__db.upsert(
      {"git": {"github_token": token, "origin": origin}},
      Token.git.exists()
    )

  def get_auth_token(self) -> dict | None:
    Token = DbQuery()
    doc = self.__db.get(Token.git.exists())
    if doc and 'git' in doc and 'github_token' in doc['git'] and 'origin' in doc['git']:
      return {"token": doc['git']['github_token'], "origin": doc['git']['origin']}
    return None


@lru_cache
def inject_git_db_service(db: TinyDB = Depends(inject_db)) -> GitDbService:
  return GitDbService(db=db)
