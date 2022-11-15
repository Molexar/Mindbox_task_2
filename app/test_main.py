import pytest
from fastapi.testclient import TestClient
from sqlalchemy import inspect

from .main import app, get_db
from db import schemas
from db import models
from db.crud import get_products_categories_m2m


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


client = TestClient(app)


def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


# def test_products_get():
#     response = client.get('/products')
#     products = next(get_db()).query(Product).all()
#     products_json = json.dumps([(dict(row.items())) for row in products])
#
#     assert len(products) == len(response.json())
#     assert products_json == response.json()
#
#
# def test_categories_get():
#     response = client.get('/categories')
#     categories = next(get_db()).query(Category).all()
#     categories_json = json.dumps([(dict(row.items())) for row in categories])
#
#     assert len(categories) == len(response.json())
#     assert categories_json == response.json()


@pytest.mark.parametrize("real,expected", [
    (client.get('/products').json(), [schemas.Product.from_orm(row)
                                      for row in next(get_db()).query(models.Product).all()]),
    (client.get('/categories').json(), [schemas.Category.from_orm(row)
                                        for row in next(get_db()).query(models.Category).all()]),
    (client.get('/products-categories').json(), [row
                                                 for row in get_products_categories_m2m(next(get_db()))])
])
def test_lists_get(real: dict, expected: dict):
    assert len(real) == len(expected)
    assert real == expected
