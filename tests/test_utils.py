from pathlib import Path

from src.Category import Category
from src.utils import load_data

DATA_PATH = Path(__file__).parent.parent / "data" / "products.json"


def test_load_data():
    data = load_data(DATA_PATH)

    assert type(data) is list
    assert len(data) == 2

    assert isinstance(data[0], Category)
    assert data[0].name == "Смартфоны"
    assert len(data[0].products) == 3

    assert isinstance(data[0].products[0], str)
    assert data[0].products[0] == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."

    assert data[1].name == "Телевизоры"
    assert len(data[1].products) == 1
