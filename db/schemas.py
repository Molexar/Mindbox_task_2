from typing import Union, List

from pydantic import BaseModel


class ProductBase(BaseModel):
    id: int
    title: str
    description: Union[str, None] = None

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class Product(ProductBase):
    categories: List[CategoryBase] = []


class Category(CategoryBase):
    products: List[ProductBase] = []
