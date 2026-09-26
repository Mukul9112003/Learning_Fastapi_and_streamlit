from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from Model.base import Base


class UserTable(Base):
    __tablename__="User"
    id:Mapped[int]=mapped_column(Integer,autoincrement=True,primary_key=True)
    username:Mapped[str]=mapped_column(String(100),unique=True)
    hassed_password:Mapped[str]=mapped_column(String(100))