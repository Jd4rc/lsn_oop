from pathlib import Path

from src.Product import Product
from src.utils import load_data
from src.Category import Category

DATA_PATH = Path(__file__).parent.parent / 'data' / 'products.json'

def test_load_data():
    data = load_data(DATA_PATH)

    assert type(data) == list
    assert len(data) == 2

    assert isinstance(data[0], Category)
    assert data[0].name == 'Смартфоны'
    assert len(data[0].products) == 3

    assert isinstance(data[0].products[0], Product)
    assert data[0].products[0].name == "Samsung Galaxy C23 Ultra"
    assert data[0].products[0].description == "256GB, Серый цвет, 200MP камера"
    assert data[0].products[0].price == 180000.0

    assert data[1].name == 'Телевизоры'
    assert len(data[1].products) == 1



