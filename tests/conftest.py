import pytest
from src.Category import Category
from src.Product import Product

@pytest.fixture
def vegetable() -> Category:
    return Category(
        name="Овощи",
        description="Свежие овощи",
        products=["Огурец", "Помидор"]
    )


@pytest.fixture
def phone() -> Product:
    return Product(
        'Pixel 5',
        '123',
        1.1,
        5,
    )

