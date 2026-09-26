from abc import ABC, abstractmethod

from schemas.user import RegisterRequest, User


class Database(ABC):

    @abstractmethod
    def create_user(
        self,
        data: RegisterRequest
    ) -> User:
        pass

    @abstractmethod
    def get_user_by_id(
        self,
        user_id: int | str
    ) -> User | None:
        pass

    @abstractmethod
    def update_user(
        self,
        user_id: int | str,
        data: RegisterRequest
    ) -> User | None:
        pass