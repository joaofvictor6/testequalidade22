import pytest
from app.service import UserService
from app.exceptions import (
    EmailAlreadyExistsException,
    InvalidPasswordException,
    InvalidCredentialsException,
)

@pytest.fixture
def user_service():
    return UserService()

# Teste 1: Criação de usuário válido
def test_register_valid_user(user_service):
    user = user_service.register_user("John Doe", "john@example.com", "Password123")
    assert user.name == "John Doe"
    assert user.email == "john@example.com"
    # Verifica se o repositório tem 1 usuário
    assert len(user_service.user_repository.users) == 1

# Teste 2: Exceção para email duplicado
def test_register_duplicate_email(user_service):
    user_service.register_user("John Doe", "john@example.com", "Password123")
    with pytest.raises(EmailAlreadyExistsException, match="Email already exists."):
        user_service.register_user("Jane Doe", "john@example.com", "Password1234")

# Teste 3: Exceção para senha inválida
def test_register_invalid_password(user_service):
    with pytest.raises(InvalidPasswordException, match="Password must be at least 8 characters and contain a number."):
        user_service.register_user("John Doe", "john@example.com", "short")

# Teste 4: Login com credenciais válidas
def test_login_valid_user(user_service):
    user_service.register_user("John Doe", "john@example.com", "Password123")
    user = user_service.login_user("john@example.com", "Password123")
    assert user.email == "john@example.com"

# Teste 5: Exceção para senha incorreta
def test_login_invalid_credentials(user_service):
    user_service.register_user("John Doe", "john@example.com", "Password123")
    with pytest.raises(InvalidCredentialsException, match="Invalid email or password."):
        user_service.login_user("john@example.com", "WrongPassword")

# Teste 6: Login com usuário não encontrado
def test_login_user_not_found(user_service):
    with pytest.raises(InvalidCredentialsException, match="Invalid email or password."):
        user_service.login_user("nonexistent@example.com", "Password123")
