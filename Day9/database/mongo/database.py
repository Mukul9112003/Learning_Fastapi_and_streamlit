from schemas.user import RegisterRequest, User

from database.base import Database


class MongoDatabase(Database):

    def __init__(self, db):
        self.db = db

    def create_user(
        self,
        data: RegisterRequest
    ) -> User:

        raise NotImplementedError

    def get_user_by_id(
        self,
        user_id: int | str
    ) -> User | None:

        raise NotImplementedError

    def update_user(
        self,
        user_id: int | str,
        data: RegisterRequest
    ) -> User | None:

        raise NotImplementedError