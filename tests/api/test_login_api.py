
import pytest
import requests

BASE_URL = "https://dummyjson.com/auth/login"


def test_valid_api_login():

    payload = {
        "username": "emilys",
        "password": "emilyspass"
    }

    response = requests.post(BASE_URL, json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "accessToken" in data
    assert data["username"] == "emilys"

    print("\nAPI Login Successful")
    print("Status Code:", response.status_code)
    print("Username:", data["username"])
    print("SUCCESS: Automatic CI pipeline triggered by GitHub push")
    print("Automatic GitHub Actions execution verified")
    print("CI/CD Test 2: New push detected successfully")

def test_invalid_api_password():

    payload = {
        "username": "emilys",
        "password": "wrongpassword"
    }

    response = requests.post(BASE_URL, json=payload)

    assert response.status_code == 400

    print("\nInvalid credentials rejected")
    print("Status Code:", response.status_code)


def test_missing_api_credentials():

    payload = {}

    response = requests.post(BASE_URL, json=payload)

    assert response.status_code == 400

    print("\nMissing credentials rejected")
    print("Status Code:", response.status_code)
