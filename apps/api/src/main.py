import uvicorn
from fastapi import FastAPI

from server_core import EnvService
from .hello import health_router as hello_router

app = FastAPI()

app.include_router(hello_router)

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
    access_log=True,
  )
