from pydantic import BaseModel,EmailStr
from typing import Optional, ClassVar 

class Blog(BaseModel):
    title: str
    body : str
    published: Optional[bool] 

class BlogResponse(BaseModel):
    title: str
    body: str

    class Config:
        from_attributes = True  # Replaces orm_mode in Pydantic v2.x

class User(BaseModel):
    Username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    Username: str
    email: EmailStr

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Show_Blog(BaseModel):
    title: str
    body: str

    writer: UserResponse
