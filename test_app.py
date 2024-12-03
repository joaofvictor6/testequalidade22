import pytest
from app import app, users

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def reset_users():
    users.clear()  # Reseta os usuários antes de cada teste
