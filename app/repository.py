from app.exceptions import EmailAlreadyExistsException

class UserRepository:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        if user.email in self.users:
            raise EmailAlreadyExistsException("Email already exists.")
        self.users[user.email] = user

    def get_user_by_email(self, email):
        return self.users.get(email)
