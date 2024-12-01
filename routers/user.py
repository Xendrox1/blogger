from fastapi import APIRouter,HTTPException, Depends
import schemas
from sqlalchemy.orm import Session
from database import get_db
from sqlalchemy import select
from repository import end_user

router= APIRouter(prefix=('/user'), tags=['User'])

@router.get('/{id}',response_model=schemas.UserResponse1)
def get_user(id:int,db: Session = Depends(get_db)):
    return end_user.get(id,db)