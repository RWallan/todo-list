from task_manager.app.controllers.tasks import Task
from task_manager.app.models.tasks_models import InputTask


def test_list_tasks_must_return_all_tasks():
    tasks = Task()
    all_tasks = tasks.list_tasks()
    assert all_tasks == []


def test_insert_new_task_must_return_the_title_description_and_id():
    new_task = InputTask(
        **{"title": "A title", "description": "A description"}
    )

    tasks = Task()

    assert list(tasks.add_task(new_task).keys()) == [
        "title",
        "description",
        "status",
        "id",
    ]
