#core/settings.py
from pydantic_settings import SettingsConfigDict,BaseSettings
class Setting(BaseSettings):
    db_url:str
    expire_time_in_minutes:int
    algorithm:str
    secret_key:str
    model_config=SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
settings = Settings()
#database/database_connection.py
from core.settings import setting
from sqlalchemy import create_engine,String,Integer,select
from sqlalchemy.orm import mapped_column,Mapped,Session,sessionmaker,DeclarativeBase
DB_URL=setting.db_url
class Base(DeclarativeBase):
    pass
engine=create_engine(DB_URL,connect_args={"check_same_thread":False})
SessionLocal=sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)
def db_session():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
#register/database/uses_db.py
from abc import ABC,abstractmethod
class database(ABC):
    @abstractmethod
    def create_user(self,data):
        pass
    @abstractmethod
    def get_user(self,id:str):
        pass
#Model/table.py
class User(Base):
    __tablename__="user"
    username:Mapped[str]=mapped_column(String(10),primary_key=True)
    hashed_password:Mapped[str]=mapped_column(String(10))
#register/database/sqldatabase.py
from Model.table import User
class SQLDatabase(database):
    def __init__(self,session:Session):
        self.session=session
    def create_user(self,data):
        statement=select(User).where(data.username==User.username)
        user=self.session.scalar(statement)
        if user:
            raise Exception("user already found")
        user = User(
        username=data.username,
        hashed_password=data.hashed_password
    )
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return "user created"       
    def get_user(self, id: str):
        segment=select(User).where(User.username==id)
        user=self.session.scalar(segment)
        if user:
            return user
        raise Exception("user not found")
#register/tokens.py
from jose import jwt,JWTError
from datetime import datetime,timedelta,timezone
class Token():
    def create_token(self,username):
        expire=datetime.now(timezone.utc)+timedelta(setting.Expire_time_in_minutes)
        payload={
            "sub":username,
            "exp":expire
        }
        token=jwt.encode(payload,setting.secret_key,algorithm=setting.Algorithm)
        return token
    def verify_token(self,token):
        try:
            payload=jwt.decode(token,setting.secret_key,algorithms=[setting.Algorithm])
            username=payload.get("sub")
            if username is None:
                raise Exception("Token not verify")
            return username
        except JWTError:
            raise Exception("Invalid token")
#schem/user.py
class register_request:
    username:str
    password:str
class login_request:
    username:str
    password:str
#service/password_servive.py
from 
class Password:
    def hashed_password(self,plain_password):
        schema(plain_password)