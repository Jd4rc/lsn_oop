from src.Category import Category


def test_category_initialization(vegetable):
    assert vegetable.name == "Овощи"
    assert vegetable.description == "Свежие овощи"
    assert vegetable.products == ["Огурец", "Помидор"]


def test_category_count():
    Category.category_count = 0
    Category.product_count = 0

    Category("Овощи", "Свежие овощи", [])
    Category("Фрукты", "Свежие фрукты", [])

    assert Category.category_count == 2


def test_product_count():
    Category.category_count = 0
    Category.product_count = 0

    Category("Овощи", "Свежие овощи", ["Кабачок", "Капуста"])
    Category("Фрукты", "Свежие фрукты", ["Клубника", "Слива"])

    assert Category.product_count == 4
