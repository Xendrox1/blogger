from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__='blogs'
    id = Column(Integer,primary_key=True, index= True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    user_id= Column(Integer, ForeignKey('User_Credentials.id'), nullable=True)
    writer = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__='User_Credentials'
    id = Column(Integer, primary_key=True, index= True)
    Username= Column(String, unique= True, index=True)
    email=Column(String, unique=True,index=True)
    password=Column(String, nullable=False)

    blogs= relationship("Blog", back_populates = "writer")