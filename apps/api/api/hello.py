from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def hello():
    """Return a friendly greeting."""
    return {"message": "Hello api"}