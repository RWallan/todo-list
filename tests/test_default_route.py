from fastapi import status
from fastapi.testclient import TestClient
from task_manager.main import app


def test_index_api_must_return_200_status_code():
    client = TestClient(app)
    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK


def test_index_api_must_return_a_message():
    expected_response = {"message": "Hi, this is my task manager API. Enjoy!"}

    client = TestClient(app)
    response = client.get("/")

    assert response.json() == expected_response
