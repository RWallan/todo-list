from fastapi import FastAPI

from task_manager.app import api_router

app = FastAPI(title="Task Manager")

app.include_router(api_router)
