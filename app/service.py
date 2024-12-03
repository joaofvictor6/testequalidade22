from app.models import User
from app.repository import UserRepository
from app.exceptions import (
    EmailAlreadyExistsException,
    InvalidPasswordException,
    InvalidCredentialsException,
)

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, name, email, password):
        if not (len(password) >= 8 and any(char.isdigit() for char in password)):
            raise InvalidPasswordException("Password must be at least 8 characters and contain a number.")
        
        user = User(name=name, email=email, password=password)
        self.user_repository.add_user(user)
        return user

    def login_user(self, email, password):
        user = self.user_repository.get_user_by_email(email)
        if not user or user.password != password:
            raise InvalidCredentialsException("Invalid email or password.")
        return user
