from fastapi import status
from fastapi.testclient import TestClient

from task_manager.app.models.tasks_models import InputTask
from task_manager.app.routes.task_route import tasks
from task_manager.main import app


def test_list_task_must_return_200_status_code():
    client = TestClient(app)
    response = client.get("tasks/tasks")

    assert response.status_code == status.HTTP_200_OK


def test_list_task_format_must_return_a_json():
    client = TestClient(app)
    response = client.get("/tasks/tasks")

    assert response.headers["Content-type"] == "application/json"


def test_list_task_must_return_a_list_of_dict():
    client = TestClient(app)
    response = client.get("/tasks/tasks")

    assert isinstance(response.json(), list)


def test_list_task_return_must_has_id():
    new_task = InputTask(
        **{
            "title": "title 1",
            "description": "description 1",
            "status": "Finalized",
        }
    )

    tasks.add_task(new_task)

    client = TestClient(app)
    response = client.get("/tasks/tasks")

    assert "id" in response.json().pop()


def test_list_task_return_must_has_title():
    new_task = InputTask(
        **{
            "title": "title 1",
            "description": "description 1",
            "status": "Finalized",
        }
    )

    tasks.add_task(new_task)

    client = TestClient(app)
    response = client.get("/tasks/tasks")

    assert "title" in response.json().pop()


def test_list_task_return_must_has_description():
    new_task = InputTask(
        **{
            "title": "title 1",
            "description": "description 1",
            "status": "Finalized",
        }
    )

    tasks.add_task(new_task)

    client = TestClient(app)
    response = client.get("/tasks/tasks")

    assert "description" in response.json().pop()


def test_list_task_return_must_has_status():
    new_task = InputTask(
        **{
            "title": "title 1",
            "description": "description 1",
            "status": "Finalized",
        }
    )

    tasks.add_task(new_task)

    client = TestClient(app)
    response = client.get("/tasks/tasks")

    assert "status" in response.json().pop()


def test_tasks_must_accept_post():
    client = TestClient(app)
    response = client.post("/tasks/tasks")

    assert response.status_code != status.HTTP_405_METHOD_NOT_ALLOWED


def test_post_task_must_have_a_title():
    client = TestClient(app)
    response = client.post("/tasks/tasks")

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_title_must_contain_between_3_50_characters():
    client = TestClient(app)
    response = client.post("/tasks/tasks", json={"title": 2 * "*"})

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    response = client.post("/tasks/tasks", json={"title": 51 * "*"})

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_post_task_must_have_a_description():
    client = TestClient(app)
    response = client.post("/tasks/tasks", json={"title": "A title"})

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_description_must_max_length_of_140_characters():
    client = TestClient(app)
    response = client.post(
        "/tasks/tasks", json={"title": "A title", "description": 141 * "*"}
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_post_task_must_be_returned():
    task_expected = {"title": "A title", "description": "A description"}

    client = TestClient(app)
    response = client.post("tasks/tasks", json=task_expected)

    task_received = response.json()

    assert task_received["title"] == task_expected["title"]
    assert task_received["description"] == task_expected["description"]


def test_post_task_must_be_a_unique_id():
    task_1 = {"title": "First title", "description": "First description"}
    task_2 = {"title": "Second title", "description": "Second description"}

    client = TestClient(app)
    response_1 = client.post("tasks/tasks", json=task_1)
    response_2 = client.post("tasks/tasks", json=task_2)

    assert response_1.json()["id"] != response_2.json()["id"]


def test_post_task_must_be_not_finalized_without_input():
    task = {"title": "A title", "description": "A description"}

    client = TestClient(app)
    response = client.post("tasks/tasks", json=task)

    assert response.json()["status"] == "Not finalized"


def test_post_task_must_return_201_status_code():
    task = {"title": "A title", "description": "A description"}

    client = TestClient(app)
    response = client.post("tasks/tasks", json=task)

    assert response.status_code == status.HTTP_201_CREATED


def test_post_task_must_persists():
    task = {"title": "A title", "description": "A description"}

    client = TestClient(app)
    client.post("tasks/tasks", json=task)

    all_tasks = tasks.list_tasks()

    assert len(all_tasks) != 0
