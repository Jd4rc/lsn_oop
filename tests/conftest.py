import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def vegetable() -> Category:
    return Category(
        name="Овощи",
        description="Свежие овощи",
        products=[
            Product("Огурец", "Короткоплодный огурец", 78.14, 5),
            Product("Помидор", "Бычье сердце", 105.51, 15),
        ],
    )


@pytest.fixture
def phone_pixel_5() -> Product:
    return Product(
        "Pixel 5",
        "123",
        1.1,
        5,
    )


@pytest.fixture
def phone_samsung_s25() -> Product:
    return Product(
        "Samsung S25",
        "456",
        1.5,
        2,
    )
