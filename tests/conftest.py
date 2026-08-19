import pytest

from config.config import BASE_URL
from src.api_client import APIClient

@pytest.fixture
def api_client():
    return APIClient(BASE_URL)