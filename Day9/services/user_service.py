from database.base import Database
from schemas.user import RegisterRequest


class UserService:

    def __init__(self, database: Database):

        self.database = database

    def register_user(self, data: RegisterRequest):

        user = self.database.create_user(data)

        return user