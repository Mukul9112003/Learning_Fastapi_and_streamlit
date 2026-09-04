from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import declarative_base,sessionmaker,Session
Base=declarative_base()
URL="sqlite:///./test.db"
engine=create_engine(URL,connect_args={"check_same_thread":False})
SessionLocal=sessionmaker(bind=engine)

def db_session():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()