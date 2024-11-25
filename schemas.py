class Blog(BaseModel):
    title: str
    body : str
    published: Optional[bool] 