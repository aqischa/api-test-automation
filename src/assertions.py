def assert_success(response):
    assert response.status_code == 200

def assert_not_found(response):
    assert response.status_code == 404

def assert_json_response(response):
    assert "application/json" in response.headers["Content-Type"]

def assert_user_response(data):
    assert isinstance(data, dict)
    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["username"], str)
    assert isinstance(data["email"], str)

def assert_post_response(data):
    assert isinstance(data, dict)
    assert isinstance(data["userId"], int)
    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)