from app.database.sql_database import create_tables
from app.dependencies.repository import get_user_repository
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.services.user_service import UserService
from fastapi import Depends, FastAPI

app = FastAPI()

create_tables()


@app.post("/users")
def create_user(
    user_data: UserCreate,
    repository: UserRepository = Depends(get_user_repository)
):
    user = User(
        name=user_data.name,
        email=user_data.email
    )

    service = UserService(repository)

    return service.create_user(user)