import pytest
from fastapi.testclient import TestClient
from importlib import import_module

app_module = import_module("06_fastapi_jwt")
app = app_module.app

client = TestClient(app)


def test_public_route():
    response = client.get("/public")
    assert response.status_code == 200
    assert "message" in response.json()


def test_me_without_token():
    response = client.get("/me")
    assert response.status_code == 401


def test_login_success():
    response = client.post("/token", data={
        "username": "rodrigo",
        "password": "secret"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_me_with_token():
    # Primeiro faz login para pegar o token
    login = client.post("/token", data={
        "username": "rodrigo",
        "password": "secret"
    })
    token = login.json()["access_token"]

    # Depois acessa /me com o token
    response = client.get("/me", headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["username"] == "rodrigo"


def test_login_wrong_password():
    response = client.post("/token", data={
        "username": "rodrigo",
        "password": "senhaerrada"
    })
    assert response.status_code == 401