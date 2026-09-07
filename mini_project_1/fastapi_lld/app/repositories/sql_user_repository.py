from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository

class SQLUserRepository(UserRepository):

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, user_id):
        return self.session.get(User, user_id)
    def save(self, user):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

        return user

    