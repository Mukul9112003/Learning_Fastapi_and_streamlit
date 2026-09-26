from config.settings import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if settings.database_url is None:
    raise Exception("DATABASE_URL not set")


engine = create_engine(
    settings.database_url,
    connect_args={
        "check_same_thread": False
    }
)

LocalSession = sessionmaker(
    bind=engine
)


def get_sql_session():

    db = LocalSession()

    try:
        yield db

    finally:
        db.close()