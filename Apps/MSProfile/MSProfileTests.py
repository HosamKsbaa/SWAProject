import pytest
from fastapi.testclient import TestClient
from .MSProfileApp import app

client = TestClient(app)

def test_create_user_profile_success():
    # Send a request to create a new user profile
    payload = {
        "userId": '123',
        "username": "john_doe",
        "email": "john.doe@example.com",
        "profilePictureUrl": "https://example.com/profile.jpg"
    }
    response = client.post("/api/profiles", json=payload)

    # Assert the response status code is 201 (Created)
    assert response.status_code == 201

    # Assert the response body contains the correct user ID
    assert response.json() == {"userId": '123'}


def test_create_user_profile_existing_id():
    # Create a user profile with an existing ID for the test
    payload = {
        "userId": '456',
        "username": "john_doe",
        "email": "john.doe@example.com",
        "profilePictureUrl": "https://example.com/profile.jpg"
    }
    response = client.post("/api/profiles", json=payload)

    # Send a request to create a user profile with the same ID
    payload = {
        "userId": '456',
        "username": "new_user",
        "email": "new.user@example.com",
        "profilePictureUrl": "https://example.com/new.jpg"
    }
    response = client.post("/api/profiles", json=payload)

    # Assert the response status code is 400 (Bad Request)
    assert response.status_code == 400

    # Assert the response body contains the correct error message
    assert response.json() == {"detail": "User ID already exists"}

def test_create_user_profile_invalid_data():
    # Send a request to create a user profile with invalid data
    payload = {
        "userId": "invalid",
        "username": "invalid_user",
        "email": "invalid.user@example.com",
        "profilePictureUrl": "https://example.com/invalid.jpg"
    }
    response = client.post("/api/profiles", json=payload)

    # Assert the response status code is 400
    assert response.status_code == 400


# Add more test cases as needed
