from uuid import uuid4

from task_manager.app.models.tasks_models import InputTask, OutputTask


class Task:
    def __init__(self) -> None:
        self.tasks: list[OutputTask] = []

    def list_tasks(self) -> list[OutputTask]:
        return self.tasks

    def _create_task_id(self) -> dict[str, str]:
        id = str(uuid4())
        return {"id": id}

    def add_task(self, task: InputTask) -> OutputTask:
        task = task.dict()
        task.update(self._create_task_id())
        self.tasks.append(task)

        return task

    def filter_task_by_id(self, id: str) -> OutputTask:
        _filtered_task = filter(lambda task: task["id"] == id, self.tasks)

        filtered_task = list(_filtered_task)[0]

        return filtered_task
