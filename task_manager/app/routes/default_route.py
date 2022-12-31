from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def index():
    return {"message": "Hi, this is my task manager API. Enjoy!"}
