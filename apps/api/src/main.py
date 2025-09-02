import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from git_server.git_router import git_router
from server_core import inject_db, EnvService, get_startup_logging_config
from .config import get_reload_dirs
from .hello import health_router as hello_router

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["http://localhost:4200", "http://localhost:4300", "http://localhost:8001"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(hello_router)
app.include_router(git_router)


@app.get("/health")
def health_check():
  try:
    db = inject_db()
    db.all()
    return {"status": "ok"}
  except Exception as e:
    raise HTTPException(status_code=503, detail=str(e))


@app.get("/")
def read_root():
  return {"message": "Hello from API"}


env = EnvService()

if __name__ == "__main__":
  uvicorn.run(
    "src.main:app",
    host="0.0.0.0",
    port=env.port,
    reload=True,
    reload_dirs=get_reload_dirs(),
    log_config=get_startup_logging_config(env),
    access_log=True,
  )
