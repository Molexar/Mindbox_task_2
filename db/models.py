from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .database import Base

class Associations(Base):
    __tablename__ = "association_table"
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'), primary_key=True)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    categories = relationship(
        "Category", secondary='association_table', back_populates="products"
    )


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)

    products = relationship(
        "Product", secondary='association_table', back_populates="categories"
    )

