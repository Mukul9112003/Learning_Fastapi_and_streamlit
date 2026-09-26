from pydantic import BaseModel, Field


class post_request_model(BaseModel):
    name:str
    id:int
    age:int = Field(ge=0)
class put_request_model(BaseModel):
    name:str 
    id:int 
    age:int = Field(ge=0)
class patch_request_model(BaseModel):
    name:str | None=None
    id:int | None=None
    age: int | None = Field(default=None, ge=0)