from fastapi import Depends, status, HTTPException
import schemas, models
from sqlalchemy.orm import Session 
from database import get_db
from sqlalchemy import select

def create(blog: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title= blog.title, body= blog.body,user_id= 1)
    db.add (new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def all(db: Session):
    statement = select(models.Blog) #select(models.Blog) is used to create a statement for retrieving all blog entries.
    result = db.execute(statement) #db.execute(statement) executes the query, which returns a result object.
    blogs = result.scalars().all() #.scalars().all() is used to get a list of models.Blog instances, similar to the query().all() approach.
    return blogs

def show(id:int, db: Session = Depends(get_db)):
    statement = select(models.Blog).where(models.Blog.id == id)
    results = db.execute(statement)
    show = results.scalars().first()
    if show is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog with the id number {id} does not exist.")
    return show    

def delete(id: int, db :Session =Depends(get_db)):
    statement = select(models.Blog).where(models.Blog.id == id)
    result = db.execute(statement)
    blog = result.scalars().first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog with the id number {id} does not exist.")
    db.delete(blog)
    db.commit()
    return{'message': f"Blog with id {id} deleted sucessfully."}

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