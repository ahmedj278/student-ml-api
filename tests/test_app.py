import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"
    assert response.json["application"] == "student-ml-api"
    assert response.json["version"] == "1.0.0"


def test_predict_success(client):
    response = client.post("/predict", json={"value": 10})

    assert response.status_code == 200
    assert response.json["input"] == 10
    assert response.json["prediction"] == 20


def test_predict_missing_input(client):
    response = client.post("/predict", json={})

    assert response.status_code == 400


def test_predict_invalid_input(client):
    response = client.post("/predict", json={"value": "hello"})

    assert response.status_code == 400