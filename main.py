from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
import uvicorn
import schemas, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import select

app=FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create_blog(blog: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title= blog.title, body= blog.body)
    db.add (new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete('/blog/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db :Session =Depends(get_db)):
    statement = select(models.Blog)
    result = db.execute(statement)
    blog = result.scalars().first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog with the id number {id} does not exist.")
    db.delete(blog)
    db.commit()
    return ("DONE") 
    
    
@app.get('/blog/all')
def all(db: Session = Depends(get_db)):
    statement = select(models.Blog) #select(models.Blog) is used to create a statement for retrieving all blog entries.
    result = db.execute(statement) #db.execute(statement) executes the query, which returns a result object.
    blogs = result.scalars().all() #.scalars().all() is used to get a list of models.Blog instances, similar to the query().all() approach.
    return blogs
    
@app.get('/blog')
def show(id:int, db: Session = Depends(get_db)):
    statement = select(models.Blog).where(models.Blog.id == id)
    results = db.execute(statement)
    show = results.scalars().first()
    if show is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog with the id number {id} does not exist.")
    return show

#if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port = 9000)

