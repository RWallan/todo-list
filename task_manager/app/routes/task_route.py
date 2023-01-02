from fastapi import APIRouter, status

import task_manager.app.models.tasks_models as task_models
from task_manager.app.controllers.tasks import Task

router = APIRouter()
tasks = Task()


@router.get("/tasks")
def list_tasks() -> list[task_models.OutputTask]:
    return tasks.list_tasks()


@router.post(
    "/tasks",
    response_model=task_models.OutputTask,
    status_code=status.HTTP_201_CREATED,
)
def create_tasks(task: task_models.InputTask) -> task_models.OutputTask:
    return tasks.add_task(task)
