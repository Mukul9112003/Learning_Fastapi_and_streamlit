from sqlalchemy import create_engine,String,Integer
from sqlalchemy.orm import sessionmaker,DeclarativeBase,Mapped,MappedColumn
from corn.settings import setting
if setting.DataBase_url is None:
    raise Exception("DataBase_url not set")
engine=create_engine(setting.DataBase_url,connect_args={"check_same_thread":False})
Local_Session=sessionmaker(bind=engine)
def get_database():
    db=Local_Session()
    try:
        yield db
    finally:
        db.close()