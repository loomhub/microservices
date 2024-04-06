from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API. Call /wiki or /search"}


def test_read_search():
    response = client.get("/search/Shahrukh")
    assert response.status_code == 200
