from abc import ABC, abstractmethod
from typing import Any
class BaseRepository(ABC):

    @abstractmethod
    def create(self, data)->Any:
        pass

    @abstractmethod
    def get_users(self)->Any:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id:Any)->Any:
        pass

    @abstractmethod
    def update_user(self, user_id:Any, data:Any)->Any:
        pass

    @abstractmethod
    def patch_user(self, user_id:Any, data)->Any:
        pass

    @abstractmethod
    def delete_user(self, user_id:Any)->Any:
        pass