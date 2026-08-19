from src.assertions import assert_success, assert_json_response

def test_get_post(api_client):
    response = api_client.get("/posts/1")

    assert_success(response)
    assert_json_response(response)

    data = response.json()

    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
