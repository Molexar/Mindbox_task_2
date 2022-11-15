from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from db import crud, models, schemas
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/products", response_model=List[schemas.Product])
async def products_list(db: Session = Depends(get_db)):
    return crud.get_products(db)


@app.get("/categories", response_model=List[schemas.Category])
async def categories_list():
    return crud.get_categories(next(get_db()))


@app.get("/products-categories")
async def m2m_products_categories():
    return crud.get_products_categories_m2m(next(get_db()))
