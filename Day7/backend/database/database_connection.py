from backend.core.settings import setting
from sqlalchemy import create_engine,Integer,Column,String
from sqlalchemy.orm import declarative_base,sessionmaker
Database_url=setting.DATABASE_URL
engine=create_engine(Database_url,connect_args={"check_same_thread":False})
sessionLocal=sessionmaker(bind=engine)
Base=declarative_base()
def db_session():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()
