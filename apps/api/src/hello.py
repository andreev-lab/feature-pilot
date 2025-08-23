from fastapi import APIRouter

health_router = APIRouter(
  prefix="/health"
)

@health_router.get("/")
def health():
    return {
      "status": "ok",
      "message": "Hello api"
    }
