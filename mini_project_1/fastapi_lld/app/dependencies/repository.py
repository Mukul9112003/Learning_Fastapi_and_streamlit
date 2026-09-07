from fastapi import Depends

from app.dependencies.database import get_db
from app.repositories.sql_user_repository import SQLUserRepository
from app.repositories.user_repository import UserRepository


def get_user_repository(
    db = Depends(get_db)
) -> UserRepository:

    return SQLUserRepository(db)