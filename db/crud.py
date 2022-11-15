from sqlalchemy.orm import Session

from . import models


def get_product(db: Session, product: int):
    return db.query(models.Product).filter(models.Product.id == product).first()


def get_category(db: Session, category: int):
    return db.query(models.Category).filter(models.Category.id == category).first()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()


def get_products_categories_m2m(db: Session, skip: int = 0, limit: int = 100):
    result = []
    for x in db.query(models.Product, models.Category).filter(
            models.Associations.product_id == models.Product.id,
            models.Associations.category_id == models.Category.id).offset(skip).limit(limit).all():
        result.append("{} - {}".format(x.Product.title, x.Category.title))
    return result
