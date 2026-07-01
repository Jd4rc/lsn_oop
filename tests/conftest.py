import pytest

from src.category import Category
from src.product import Product

@pytest.fixture
def phone_pixel_5() -> Product:
    return Product(
        "Pixel 5",
        "123",
        1.1,
        5,
    )

@pytest.fixture
def phone_iphone_16() -> Product:
    return Product(
        "iPhone 16",
        "Флагманский смартфон Apple",
        4299.99,
        10,
    )

@pytest.fixture
def phone_samsung_s24() -> Product:
    return Product(
        "Samsung Galaxy S24",
        "Флагманский смартфон Samsung",
        3899.99,
        8,
    )


@pytest.fixture
def phone_samsung_s25() -> Product:
    return Product(
        "Samsung S25",
        "456",
        1.5,
        2,
    )

@pytest.fixture
def cucumber() -> Product:
     return Product(
         "Огурец",
         "Короткоплодный огурец",
         78.14,
         5)


@pytest.fixture
def tomato() -> Product:
    return Product(
    "Помидор",
    "Бычье сердце",
    105.51,
    15)


@pytest.fixture
def vegetable(cucumber, tomato) -> Category:
    return Category(
        name="Овощи",
        description="Свежие овощи",
        products=[cucumber, tomato],
    )

@pytest.fixture
def smartphones(phone_pixel_5, phone_iphone_16, phone_samsung_s24, phone_samsung_s25, ) -> Category:
    return Category(
        name="Смартфоны",
        description="Современные смартфоны",
        products=[phone_pixel_5, phone_iphone_16, phone_samsung_s24, phone_samsung_s25],
    )

