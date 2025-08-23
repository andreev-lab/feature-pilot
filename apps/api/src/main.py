import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from server_core import EnvService
from .hello import health_router as hello_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hello_router)

@app.get("/")
def read_root():
    return {"message": "Hello from API"}


state = 0

@app.get('/state')
def get_state():
  return {
    "state": state
  }

@app.put('/state')
def increment_state():
  global state
  state += 1
  if state % 5 == 0:
    raise HTTPException(status_code=400, detail=f"The state ({state}) is a multiple of 5!")
  return get_state()

env = EnvService()

if __name__ == "__main__":
  uvicorn.run(
    "src.main:app",
    host="0.0.0.0",
    port=env.port,
    reload=True,
    access_log=True,
  )
