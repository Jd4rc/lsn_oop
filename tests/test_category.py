import pytest

from src.category import Category


def test_category_initialization(vegetable):
    assert vegetable.name == "Овощи"
    assert vegetable.description == "Свежие овощи"
    assert len(vegetable.products) == 2


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


def test_add_product(phone_pixel_5, vegetable):
    vegetable.add_product(phone_pixel_5)

    assert phone_pixel_5 in vegetable.products
    assert len(vegetable.products) == 3


def test_add_product_increases_product_count(phone_pixel_5, vegetable):
    initial_count = Category.product_count

    vegetable.add_product(phone_pixel_5)

    assert vegetable.product_count == initial_count + 1


def test_add_multiple_product(phone_pixel_5, phone_samsung_s25, vegetable):

    vegetable.add_product(phone_pixel_5)
    vegetable.add_product(phone_samsung_s25)

    assert len(vegetable.products) == 4
    assert phone_pixel_5 in vegetable.products
    assert phone_samsung_s25 in vegetable.products


def test_category_add_product_another_class():

    category = Category("Смартфоны", "Высокотехнологичные смартфоны", [])

    with pytest.raises(TypeError, match="Ожидался Product, получен str"):
        category.add_product("123")


def test_add_invalid_product_does_not_change_category(vegetable):
    init_count = Category.product_count
    init_len = len(vegetable.products)

    with pytest.raises(TypeError):
        vegetable.add_product("123")

    assert vegetable.product_count == init_count
    assert len(vegetable.products) == init_len


def test_get_product(vegetable):
    assert str(vegetable.products[0]) == "Огурец, 78.14 руб. Остаток: 5 шт."

    assert str(vegetable.products[1]) == "Помидор, 105.51 руб. Остаток: 15 шт."


def test_category_len(vegetable):
    assert len(vegetable) == 2


def test_category_str(vegetable):
    assert str(vegetable) == f"Овощи, количество продуктов: {len(vegetable)} шт."


def test_category_total_quantity(vegetable):
    assert vegetable.total_quantity == 20


def test_category_iteration(vegetable):
    products = list(vegetable)

    assert str(products[0]) == "Огурец, 78.14 руб. Остаток: 5 шт."
    assert str(products[1]) == "Помидор, 105.51 руб. Остаток: 15 шт."


def test_category_stop_iteration(vegetable):
    products = iter(vegetable)

    next(products)
    next(products)
    with pytest.raises(StopIteration):
        next(products)
