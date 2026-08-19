from src.assertions import (
    assert_success,
    assert_json_response,
    assert_post_response,
)

def test_get_post(api_client):
    response = api_client.get("/posts/1")

    assert_success(response)
    assert_json_response(response)

    data = response.json()

    assert_post_response(data)

    assert data["id"] == 1