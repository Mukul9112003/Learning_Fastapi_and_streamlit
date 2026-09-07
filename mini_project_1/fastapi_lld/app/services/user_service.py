from app.repositories.user_repository import UserRepository


class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user):
        return self.repository.save(user)