from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):

    username: EmailStr

    password: str = Field(
        min_length=8
    )

    age: int = Field(
        ge=18,
        le=100
    )

    name: str = Field(
        min_length=2,
        max_length=100
    )

    phone_number: str = Field(
        min_length=10,
        max_length=10,
        pattern=r"^\d{10}$"
    )


class UserResponse(BaseModel):

    id: int
    username: EmailStr
    name: str
    phone_number: str

class User(BaseModel):
    id: int | str
    username: EmailStr
    name: str
    phone_number: str