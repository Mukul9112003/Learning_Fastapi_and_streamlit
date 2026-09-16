from abc import ABC,abstractmethod
from typing import Any
class DataBase(ABC):
    @abstractmethod
    def save_data(self,Data:dict)->str:
        pass
    @abstractmethod
    def get_by_id(self,record_id:str)-> dict[str, Any] | None:
        pass