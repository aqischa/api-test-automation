import requests

def test_get_user():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"

def test_get_nonexistent_user():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/999"
    )

    assert response.status_code == 404