from pydantic import BaseModel,Field
class patient_create_request_model(BaseModel):
    name:str | None=None
    age:int=Field(... , ge=0)