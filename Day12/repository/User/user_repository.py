from abc import ABC, abstractmethod


class UserRepository(ABC):

    @abstractmethod
    def create(self, user):
        pass

    @abstractmethod
    def get_by_email(self, email):
        pass

    @abstractmethod
    def get_by_id(self, user_id):
        pass

    @abstractmethod
    def get_all(self)->any:
        pass

    @abstractmethod
    def delete(self, email):
        pass