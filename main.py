from fastapi import FastAPI, Depends
from typing import Optional
import uvicorn
import schemas, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app=FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog')
def create_blog(blog: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title= blog.title, body= blog.body)
    db.add (new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

#if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port = 9000)

