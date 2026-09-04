from sqlalchemy import Column, String

from database.database_connection import Base


class User(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True)
    password = Column(String)