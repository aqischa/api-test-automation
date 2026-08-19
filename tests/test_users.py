import pytest

from src.assertions import (
    assert_success,
    assert_not_found,
    assert_json_response,
    assert_user_response,
)

def test_get_user(api_client):
    response = api_client.get("/users/1")

    assert_success(response)
    assert_json_response(response)

    data = response.json()

    assert_user_response(data)
    
    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"

def test_get_all_users(api_client):
    response = api_client.get("/users")

    assert_success(response)
    assert_json_response(response)

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

@pytest.mark.parametrize(
    "endpoint",
    [
        "/users/999",
        "/posts/999",
        "/users/9999",
        "/posts/9999",
    ],
)
def test_get_nonexistent_resource(api_client, endpoint):
    response = api_client.get(endpoint)

    assert_not_found(response)