#this is api testing
import os
import requests
import pytest

BASE_URL = os.getenv("API_BASE_URL", "https://reqres.in/api")
HEADERS = {"x-api-key": os.getenv("REQRES_API_KEY", "reqres-free-v1")}

@pytest.mark.api
def test_get_single_user_success():
    response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS, timeout=20)
    assert response.status_code == 200
    body = response.json()
    assert set(body) >= {"data", "support"}
    assert body["data"]["id"] == 2
    assert {"email", "first_name", "last_name", "avatar"} <= set(body["data"])

@pytest.mark.api
def test_post_create_user_success():
    payload = {"name": "QA Engineer", "job": "Tester"}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS, timeout=20)
    assert response.status_code == 201
    body = response.json()
    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
    assert "id" in body and "createdAt" in body

@pytest.mark.api
def test_post_missing_data_validation_behavior():
    # ReqRes is a demo API; it may accept an empty JSON body. Assert and document
    # the actual contract rather than assuming server-side validation exists.
    response = requests.post(f"{BASE_URL}/users", json={}, headers=HEADERS, timeout=20)
    assert response.status_code in (201, 400, 422)
    body = response.json()
    assert isinstance(body, dict)
    if response.status_code == 201:
        assert "id" in body and "createdAt" in body
    else:
        assert isinstance(body, dict)

@pytest.mark.api
def test_get_unknown_user_returns_404():
    response = requests.get(f"{BASE_URL}/users/999999", headers=HEADERS, timeout=20)
    assert response.status_code == 404
    assert response.json() == {}

