from fastapi import APIRouter

from task_manager.app.routes import default

api_router = APIRouter()

api_router.include_router(default.router, tags=["default"])
