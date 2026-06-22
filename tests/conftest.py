import pytest
from src.Category import Category

@pytest.fixture
def vegetable() -> Category:
    return Category(
        name="Овощи",
        description="Свежие овощи",
        products=[]
    )

