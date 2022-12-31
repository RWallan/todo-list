from fastapi import APIRouter

from task_manager.app.routes import default_route, task_route

api_router = APIRouter()

api_router.include_router(default_route.router, tags=["default"])
api_router.include_router(task_route.router, prefix="/tasks", tags=["tasks"])
