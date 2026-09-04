from pydantic import BaseModel,Field
class create_request(BaseModel):
    email:str=Field(...)
    password:str=Field(...)
class login_request(BaseModel):
    email: str
    password: str