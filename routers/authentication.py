from fastapi import APIRouter, Depends
import schemas
from sqlalchemy.orm import Session
from repository import end_user
from database import get_db

router= APIRouter(tags=["Authentication"])

@router.post('/login',response_model=schemas.Token)
def login_user(request: schemas.UserLogin, db: Session = Depends(get_db)):   
    return end_user.login(request,db)


@router.post('/sign-up',)
def create_user( request:schemas.User, db :Session =Depends(get_db)):
    return end_user.create(request,db)