import pytest

from src.category import Category, DebitPaymentProcessor, CreditPaymentProcessor
from src.category import Order
from src.product import InvalidQuantityError
from src.product import Product


def test_category_initialization(vegetable):
    assert vegetable.name == "Овощи"
    assert vegetable.description == "Свежие овощи"
    assert len(vegetable.products_list) == 2


def test_products_returns_string_with_all_products(vegetable):

    assert vegetable.products == "Огурец, 78.14 руб. Остаток: 5 шт.\nПомидор, 105.51 руб. Остаток: 15 шт."


def test_products_returns_empty_string_when_category_is_empty():

    category = Category(
        name="Овощи",
        description="Свежие овощи",
        products=[],
    )

    assert category.products == ""


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

    assert phone_pixel_5 in vegetable.products_list
    assert len(vegetable.products_list) == 3


def test_add_product_increases_product_count(phone_pixel_5, vegetable):
    initial_count = Category.product_count

    vegetable.add_product(phone_pixel_5)

    assert vegetable.product_count == initial_count + 1


def test_add_multiple_product(phone_pixel_5, phone_samsung_s25, vegetable):

    vegetable.add_product(phone_pixel_5)
    vegetable.add_product(phone_samsung_s25)

    assert len(vegetable.products_list) == 4
    assert phone_pixel_5 in vegetable.products_list
    assert phone_samsung_s25 in vegetable.products_list


def test_category_add_product_another_class():

    category = Category("Смартфоны", "Высокотехнологичные смартфоны", [])

    with pytest.raises(TypeError, match="Ожидался Product, получен str"):
        category.add_product("123")


def test_add_invalid_product_does_not_change_category(vegetable):
    init_count = Category.product_count
    init_len = len(vegetable.products_list)

    with pytest.raises(TypeError):
        vegetable.add_product("123")

    assert vegetable.product_count == init_count
    assert len(vegetable.products_list) == init_len


def test_get_product(vegetable):
    assert str(vegetable.products_list[0]) == "Огурец, 78.14 руб. Остаток: 5 шт."

    assert str(vegetable.products_list[1]) == "Помидор, 105.51 руб. Остаток: 15 шт."


def test_category_len(vegetable):
    assert len(vegetable) == 2


def test_category_str(vegetable):
    assert str(vegetable) == f"Овощи, количество продуктов: {len(vegetable)} шт."


def test_category_total_quantity(vegetable):
    assert vegetable.total_quantity == 20


def test_category_iteration(vegetable):
    products_list = list(vegetable)

    assert str(products_list[0]) == "Огурец, 78.14 руб. Остаток: 5 шт."
    assert str(products_list[1]) == "Помидор, 105.51 руб. Остаток: 15 шт."


def test_category_stop_iteration(vegetable):
    products_list = iter(vegetable)

    next(products_list)
    next(products_list)
    with pytest.raises(StopIteration):
        next(products_list)


def test_make_order():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    order = Order()
    order.add_item(product1, 2)

    assert order.items == [(product1, 2)]
    assert order.total_price == 360000.0


def test_order_str():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    order = Order()
    order.add_item(product1, 2)

    assert str(order) == ("Заказ: Samsung Galaxy S23 Ultra: 2, На сумму: 360000.0 руб")


def test_middle_price_access(vegetable):
    assert (
        vegetable.middle_price()
        == sum(product.price * product.quantity for product in vegetable.products_list) / vegetable.total_quantity
    )


def test_middle_price_with_empty_category(fruits):
    assert fruits.middle_price() == 0


def test_make_order_with_quantity_zero():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    with pytest.raises(InvalidQuantityError, match="Недопустимое количество товара: 0"):
        order = Order()

        order.add_item(product1, 0)


def test_make_order_with_quantity_negative():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    with pytest.raises(InvalidQuantityError, match="Недопустимое количество товара: -2"):
        order = Order()

        order.add_item(product1, -2)


def test_make_order_with_quantity_over():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    order = Order()

    order.add_item(product1, 6)
    assert str(order) == (f"Заказ: Samsung Galaxy S23 Ultra: 6, На сумму: {product1.price * 6} руб")


@pytest.mark.parametrize(
    'payment_cls, payment_type',
    [
        (DebitPaymentProcessor, 'дебетового'),
        (CreditPaymentProcessor, 'кредитного'),
    ],
)
def test_payment_processor(payment_cls, payment_type, order, capsys):
    processor = payment_cls()

    processor.pay(order, '123')

    message = capsys.readouterr()

    assert f'Обработка {payment_type} типа платежа\nПроверка кода безопасности: 123' in message.out
    assert order.status == "paid"