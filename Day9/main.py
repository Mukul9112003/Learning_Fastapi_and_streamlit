from database.base import Database
from database.dependencies import get_database
from database.sql.base import Base
from database.sql.connection import engine
from fastapi import Depends, FastAPI
from schemas.user import RegisterRequest, UserResponse
from services.user_service import UserService

app = FastAPI()


Base.metadata.create_all(engine)


@app.post(
    "/register",
    response_model=UserResponse
)
def register_user(
    data: RegisterRequest,
    database: Database = Depends(get_database)
):

    service = UserService(database)

    user = service.register_user(data)

    return user