from models.user import UserTable
from schemas.user import User
from sqlalchemy import select

from database.base import Database


class SQLDatabase(Database):

    def __init__(self, db):
        self.db = db

    def create_user(self, data):

        user = UserTable(
            username=data.username,
            hashed_password=data.password,
            name=data.name,
            phone_number=data.phone_number
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return User(
    id=user.id,
    username=user.username,
    name=user.name,
    phone_number=user.phone_number
)

    def get_user_by_id(self, user_id):

        statement = select(UserTable).where(
            UserTable.id == user_id
        )

        return self.db.scalar(statement)

    def update_user(self, user_id, data):

        statement = select(UserTable).where(
            UserTable.id == user_id
        )

        user = self.db.scalar(statement)

        if user is None:
            return None

        user.username = data.username
        user.name = data.name
        user.phone_number = data.phone_number

        self.db.commit()
        self.db.refresh(user)

        return user