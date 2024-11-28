from pydantic import BaseModel,EmailStr
from typing import Optional

class Blog(BaseModel):
    title: str
    body : str
    published: Optional[bool] 
    
# class BlogReturn(Blog):
#     from_attributes= True
    
class User(BaseModel):
    Username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    Username: str
    email: EmailStr

    # class Config:
    #     from_attributes= True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Show_Blog(BaseModel):
    title: str
    body: str

    writer: UserResponse

    # class Config:
    #     from_attributes= True