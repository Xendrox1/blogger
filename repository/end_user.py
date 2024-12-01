from fastapi import HTTPException, Depends
import hashing
import models
import schemas
from sqlalchemy.orm import Session
from database import get_db
from sqlalchemy import select
from jwt_token import create_access_token
import pdb


def login(request: schemas.UserLogin, db: Session = Depends(get_db)):
    stmt = select(models.User).where(models.User.email ==
                                     request.email)  # New query syntax
    user = db.execute(stmt).scalars().first()  # Execute and fetch the result
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Verify the password
    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid password")

    # generate JWT Token and return
    access_token = create_access_token(
        data={ "username": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


def get(id: int, db: Session = Depends(get_db)):
    statement = select(models.User).where(models.User.id == id)
    user = db.execute(statement).scalars().first()
    if not user:
        raise HTTPException(
            status_code=404, detail=f"User with id {id} not found")
    return user


def create(request: schemas.User, db: Session = Depends(get_db)):
    # Check if the user already exists
    if db.query(models.User).filter(models.User.email == request.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    # hash the password
    hashedPassword = hashing.hash_password(request.password)

    new_user = models.User(Username=request.Username,
                           email=request.email, password=hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
