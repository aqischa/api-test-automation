import pytest

def test_get_user(api_client):
    response = api_client.get("/users/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"

def test_get_all_users(api_client):
    response = api_client.get("/users")

    assert response.status_code == 200

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

    assert response.status_code == 404