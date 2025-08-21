import uvicorn
from fastapi import FastAPI
from api.hello import router as hello_router

app = FastAPI()

app.include_router(hello_router)

@app.get("/")
def read_root():
    return {"message": "Hello from API"}

if __name__ == "__main__":
  uvicorn.run(
    "main:app",
    host="0.0.0.0",
    port=3000,
    reload=True,
    access_log=True,
  )
