from Model.user_table import UserTable
from repository.User.User import DataBase
from sqlalchemy import select
from sqlalchemy.orm import Session


class Sql_Database(DataBase):
    def __init__(self,session:Session):
        self.db=session
    def get_by_id(self, record_id:str):
        statement = select(UserTable).where(
            UserTable.username == record_id
        )
        user=self.db.scalar(statement)
        if user is None:
            return None

        return {
            "id": user.id,
            "username": user.username
        }
    def save_data(self,Data):
        user=UserTable(username=Data["username"],hassed_password=Data["hassed_password"])
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)   
        return "create user"   
    
class Mongo_DataBase(DataBase):
    def save_data(self,Data:dict):
        return "Save in Mongodb"
    def get_by_id(self, record_id: str):
        return None