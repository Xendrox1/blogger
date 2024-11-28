from fastapi import APIRouter,HTTPException, Depends
import hashing,models,schemas
from sqlalchemy.orm import Session
from database import get_db
from sqlalchemy import select

router= APIRouter()

@router.post('/user/login',tags= ['user'])
def login_user(request: schemas.UserLogin, db: Session = Depends(get_db),tags= ['user']):
    stmt = select(models.User).where(models.User.email == request.email)  # New query syntax
    user = db.execute(stmt).scalars().first()  # Execute and fetch the result
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Verify the password
    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid password")
    
    return {"message": "Login successful"}

@router.get('/user/{id}',tags= ['user'])
def get_user(id:int,db: Session = Depends(get_db)):
    statement=select(models.User).where(models.User.id == id)
    user = db.execute(statement).scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail= f"User with id {id} not found")
    return user

@router.post('/user/sign-up', tags= ['user'])
def create_user( request:schemas.User, db :Session =Depends(get_db)):
        # Check if the user already exists
    if db.query(models.User).filter(models.User.email == request.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    #hash the password
    hashedPassword= hashing.hash_password(request.password)

    new_user= models.User(Username=request.Username, email=request.email, password=hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user