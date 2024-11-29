from fastapi import APIRouter,HTTPException, Depends
import hashing,models,schemas
from sqlalchemy.orm import Session
from database import get_db
from sqlalchemy import select
from repository import end_user

router= APIRouter(prefix=('/user'), tags=['User'])

@router.post('/login',response_model=schemas.UserResponse2)
def login_user(request: schemas.UserLogin, db: Session = Depends(get_db)):   
    return end_user.login(request,db)

@router.get('/{id}',response_model=schemas.UserResponse2)
def get_user(id:int,db: Session = Depends(get_db)):
    return end_user.get(id,db)

@router.post('/sign-up',)
def create_user( request:schemas.User, db :Session =Depends(get_db)):
    return end_user.create(request,db)