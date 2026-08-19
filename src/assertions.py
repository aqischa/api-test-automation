def assert_success(response):
    assert response.status_code == 200

def assert_not_found(response):
    assert response.status_code == 404

def assert_json_response(response):
    assert "application/json" in response.headers["Content-Type"]