from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__='blogs'
    id = Column(Integer,primary_key=True, index= True)
    title = Column(String(225), nullable=False)
    body = Column(String, nullable=False)
    user_id= Column(Integer, ForeignKey('users.id'), nullable=True)
    writer = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True, index= True)
    Username= Column(String(50), unique= True, index=True)
    email=Column(String(100), unique=True,index=True)
    password=Column(String(225), nullable=False)

    blogs= relationship("Blog", back_populates = "writer")