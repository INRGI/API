from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter

from database import Base,engine,SessionLocal
from models import Article
from schemas import ArticleCreate,ArticleView


def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()

app = FastAPI()

Base.metadata.create_all(bind=engine)

router = SQLAlchemyCRUDRouter(
    schema=ArticleView,
    create_schema=ArticleCreate,
    db_model=Article,
    db=get_db,
    prefix='articles'
)
app.include_router(router)
