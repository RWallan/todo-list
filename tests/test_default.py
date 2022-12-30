from fastapi.testclient import TestClient
from fastapi import status
from task_manager.manager import app, TASKS


def test_list_task_must_return_200_status_code():
    client = TestClient(app)
    response = client.get("/tasks")

    assert response.status_code == status.HTTP_200_OK

def test_list_task_format_must_return_a_json():
    client = TestClient(app)
    response = client.get("/tasks")

    assert response.headers["Content-type"] == "application/json"

def test_list_task_must_return_a_list():
    client = TestClient(app)
    response = client.get("/tasks")

    assert isinstance(response.json(), list)

def test_list_task_return_must_has_id():
    TASKS.append(
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "title": "title 1",
            "description": "description 1",
            "status": "finalizado",
        }
    )
    
    client = TestClient(app)
    response = client.get("/tasks")

    assert "id" in response.json().pop()

    TASKS.clear()

def test_list_task_return_must_has_title():
    TASKS.append(
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "title": "title 1",
            "description": "description 1",
            "status": "finalizado",
        }
    )
    
    client = TestClient(app)
    response = client.get("/tasks")

    assert "title" in response.json().pop()

    TASKS.clear()

def test_list_task_return_must_has_description():
    TASKS.append(
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "title": "title 1",
            "description": "description 1",
            "status": "finalizado",
        }
    )
    
    client = TestClient(app)
    response = client.get("/tasks")

    assert "description" in response.json().pop()

    TASKS.clear()

def test_list_task_return_must_has_status():
    TASKS.append(
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "title": "title 1",
            "description": "description 1",
            "status": "finalizado",
        }
    )
    
    client = TestClient(app)
    response = client.get("/tasks")

    assert "status" in response.json().pop()

    TASKS.clear()
