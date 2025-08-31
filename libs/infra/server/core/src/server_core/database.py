from functools import lru_cache

from tinydb import TinyDB, Query as DbQuery


@lru_cache(maxsize=1)
def inject_db():
  db = TinyDB('db.json')
  return db

__all__ = ["inject_db", "DbQuery"]


