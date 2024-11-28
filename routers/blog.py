from fastapi import APIRouter, Depends, status, HTTPException 
import schemas, models
from sqlalchemy.orm import Session 
from database import  SessionLocal, get_db
from sqlalchemy import select

router = APIRouter()

@router.post('/blog')
def create_blog(blog: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title= blog.title, body= blog.body)
    db.add (new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get('/blog/all', response_model= list[schemas.Show_Blog], tags=["Blog"] )
def all(db: Session = Depends(get_db)):
    statement = select(models.Blog) #select(models.Blog) is used to create a statement for retrieving all blog entries.
    result = db.execute(statement) #db.execute(statement) executes the query, which returns a result object.
    blogs = result.scalars().all() #.scalars().all() is used to get a list of models.Blog instances, similar to the query().all() approach.
    return blogs
    

@router.get('/blog/{id}',status_code=200,response_model=schemas.Show_Blog, tags=["Blog"])
def show(id:int, db: Session = Depends(get_db)):
    statement = select(models.Blog).where(models.Blog.id == id)
    results = db.execute(statement)
    show = results.scalars().first()
    if show is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog with the id number {id} does not exist.")
    return show

@router.delete('/blog/delete/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Blog"])
def delete_blog(id: int, db :Session =Depends(get_db)):
    statement = select(models.Blog)
    result = db.execute(statement)
    blog = result.scalars().first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog with the id number {id} does not exist.")
    db.delete(blog)
    db.commit()
    return ("DONE") 

@router.put('/blog/update/{id}', status_code=status.HTTP_202_ACCEPTED, tags=["Blog"])
def update(blog_update: schemas.Blog, id:int, db: Session = Depends(get_db)):
    statement = select(models.Blog).where(models.Blog.id == id)
    results = db.execute(statement)
    blog= results.scalars().first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog with the id number {id} does not exist.")
    
    blog.title = blog_update.title
    blog.body = blog_update.body

    db.commit()
    db.refresh(blog)
    return{"message": "Blog updated successfully"}