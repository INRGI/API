from pydantic import BaseModel

class ArticleCreate(BaseModel):
    title: str
    text: str
    class Config:
        orm_mode = True

class ArticleView(ArticleCreate):
    id: int
