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

class BlogResponse(BaseModel):
    title: str
    body: str
    writer: Optional[UserResponse] = None

class Show_Blog(BaseModel):
    title: str
    body: str

class UserResponse1(BaseModel):
    Username: str
    email: EmailStr
    blogs: list[Show_Blog] = []

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[EmailStr] = None
    