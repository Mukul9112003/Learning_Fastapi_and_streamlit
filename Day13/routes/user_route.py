from fastapi import APIRouter, Depends
from pydantic import BaseModel, EmailStr
from repository.UserRepository import UserRepository
from service.user_service import UserService


class UserRequest(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str


class UserPatch(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None


def get_user_service():
    repository = UserRepository()

    return UserService(repository)


routes = APIRouter()


@routes.post("/users")
def create_user(
    data: UserRequest,
    user: UserService = Depends(get_user_service)
):
    return user.create_user(data)


@routes.get("/users")
def get_users(
    user: UserService = Depends(get_user_service)
):
    return user.get_users()


@routes.get("/users/{user_id}")
def get_user_by_id(
    user_id: int,
    user: UserService = Depends(get_user_service)
):
    return user.get_user_by_id(user_id)


@routes.put("/users/{user_id}")
def update_user(
    user_id: int,
    data: UserRequest,
    user: UserService = Depends(get_user_service)
):
    return user.update_user(user_id, data)


@routes.patch("/users/{user_id}")
def patch_user(
    user_id: int,
    data: UserPatch,
    user: UserService = Depends(get_user_service)
):
    return user.patch_user(user_id, data)


@routes.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    user: UserService = Depends(get_user_service)
):
    return user.delete_user(user_id)