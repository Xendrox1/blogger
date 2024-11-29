from pydantic import BaseModel,EmailStr
from typing import Optional, ClassVar 

class Blog(BaseModel):
    title: str
    body : str

class User(BaseModel):
    Username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    Username: str
    email: EmailStr

class UserResponse2(BaseModel):
    Username: str
    email: EmailStr
    blogs: Optional[Blog] = None

class BlogResponse(BaseModel):
    title: str
    body: str
    writer: Optional[UserResponse] = None

class Show_Blog(BaseModel):
    title: str
    body: str

