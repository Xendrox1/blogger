from fastapi import APIRouter, Depends, status, HTTPException 
import schemas
from sqlalchemy.orm import Session 
from database import get_db
from repository import blogger

router = APIRouter(prefix="/blog",tags=['Blogs'])

@router.post('/', response_model=schemas.Show_Blog)
def create_blog(blog: schemas.Blog, db: Session = Depends(get_db)):
   return blogger.create(blog,db)

@router.get('/all', response_model=list[schemas.BlogResponse] )
def all(db: Session = Depends(get_db)):
    return blogger.all(db)
    

@router.get('/{id}',status_code=200, response_model=schemas.BlogResponse)
def show(id:int, db: Session = Depends(get_db)):
    return blogger.show(id,db)

@router.delete('/delete/{id}', status_code=status.HTTP_202_ACCEPTED)
def delete_blog(id: int, db :Session =Depends(get_db)):
    return blogger.delete(id,db)

@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(blog_update: schemas.Blog, id:int, db: Session = Depends(get_db)):
    return blogger.update(blog_update, id, db)