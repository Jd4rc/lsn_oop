from src.Category import Category


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

def test_add_product(phone_pixel_5,vegetable):
   vegetable.add_product(phone_pixel_5)

   assert len(vegetable.products) == 3


def test_add_product_increases_product_count(phone_pixel_5,vegetable):
    initial_count = vegetable.product_count

    vegetable.add_product(phone_pixel_5)

    assert vegetable.product_count == initial_count + 1

def test_add_multiple_product(phone_pixel_5, phone_samsung_s25, vegetable):

    vegetable.add_product(phone_pixel_5)
    vegetable.add_product(phone_samsung_s25)

    assert len(vegetable.products) == 4


def test_get_product(vegetable):
    assert vegetable.products == ['Огурец, 78.14 руб. Остаток: 5 шт.', 'Помидор, 105.51 руб. Остаток: 15 шт.']



