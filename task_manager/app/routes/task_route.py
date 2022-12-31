from uuid import uuid4

from fastapi import APIRouter, status

import task_manager.app.models.tasks_models as task_models

router = APIRouter()


@router.get("/tasks")
def list_tasks():
    return task_models.TASKS


@router.post(
    "/tasks",
    response_model=task_models.OutputTask,
    status_code=status.HTTP_201_CREATED,
)
def create_tasks(task: task_models.InputTask):
    new_task = task.dict()
    new_task.update({"id": uuid4()})
    task_models.TASKS.append(new_task)

    return new_task
