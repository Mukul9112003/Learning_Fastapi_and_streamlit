from sqlalchemy import Column,String 
from .database_connection import Base
class user(Base):
    __tablename__="user"
    user_name=Column(String,primary_key=True)
    password=Column(String)
