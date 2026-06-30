from unittest.mock import Mock

import pytest

from src.product import Product, Smartphone, LawnGrass


def test_product_initialization_1(phone_pixel_5):
    assert phone_pixel_5.name == "Pixel 5"
    assert phone_pixel_5.description == "123"
    assert phone_pixel_5.price == 1.1
    assert phone_pixel_5.quantity == 5


def test_product_initialization_2():
    pixel_10 = Product("Pixel 10", "123", 150.0, 5)

    assert pixel_10.name == "Pixel 10"
    assert pixel_10.description == "123"
    assert pixel_10.price == 150.0
    assert pixel_10.quantity == 5


def test_new_product():
    old_products = [Product("Old Product", "123", 150.0, 5)]

    new_data = {
        "name": "New Product",
        "description": "456",
        "price": 170.0,
        "quantity": 4,
    }

    product = Product.new_product(new_data, old_products)

    assert isinstance(product, Product)
    assert product.name == "New Product"
    assert product.description == "456"
    assert product.price == 170.0
    assert product.quantity == 4


def test_new_product_with_dublicates():
    old_product = Product("Iphone 7", "32gb", 150.0, 8)

    products = [old_product]

    data = {"name": "Iphone 7", "price": 891.0, "quantity": 4}

    product = Product.new_product(data, products)

    assert product.price == 891.0
    assert product.quantity == 12


def test_new_product_with_less_price():
    old_product = Product("Iphone 7", "32gb", 150.0, 8)

    products = [old_product]

    data = {"name": "Iphone 7", "price": 100.151, "quantity": 4}

    product = Product.new_product(data, products)

    assert product.price == 150.0
    assert product.quantity == 12


def test_new_product_with_invalid_price():
    data = {"name": "Iphone 7", "description": "123", "price": 0, "quantity": 4}

    with pytest.raises(ValueError):
        Product.new_product(data, [])


def test_price_setter_with_accept_lower_price(monkeypatch):
    mock_input = Mock(return_value="y")

    monkeypatch.setattr("builtins.input", mock_input)

    product = Product("Iphone 7", "32gb", 150.0, 8)

    product.price = 100

    mock_input.assert_called_once()
    assert product.price == 100


def test_price_setter_with_reject_lower_price(monkeypatch):
    mock_input = Mock(return_value="n")

    monkeypatch.setattr("builtins.input", mock_input)

    product = Product("Iphone 7", "32gb", 150.0, 8)

    product.price = 100

    mock_input.assert_called_once()
    assert product.price == 150


def test_product_str(phone_pixel_5, phone_samsung_s25):
    assert str(phone_pixel_5) == "Pixel 5, 1.1 руб. Остаток: 5 шт."
    assert str(phone_samsung_s25) == "Samsung S25, 1.5 руб. Остаток: 2 шт."


def test_product_add(phone_pixel_5, phone_samsung_s25):
    assert phone_pixel_5 + phone_samsung_s25 == (5 * 1.1) + (2 * 1.5)

def test_smartphone_init():
    smartphone = Smartphone(
        "Samsung S25",
        'Флагман',
        150000.124,
        2,
        96,
        'Basic',
        512,
        'Black'

    )

    assert smartphone.name == "Samsung S25"
    assert smartphone.description == 'Флагман'
    assert smartphone.price == 150000.124
    assert smartphone.quantity == 2
    assert smartphone.efficiency == 96
    assert smartphone.model == 'Basic'
    assert smartphone.memory == 512
    assert smartphone.color == 'Black'

def test_lawngrass_init():
    lawngrass = LawnGrass(
        "Lawn Grass",
        'Трава высокая',
        2500,
        5,
        'Dutch',
        14,
        'Bright green'
    )

    assert lawngrass.name == "Lawn Grass"
    assert lawngrass.description == 'Трава высокая'
    assert lawngrass.price == 2500
    assert lawngrass.quantity == 5
    assert lawngrass.country == 'Dutch'
    assert lawngrass.germination_period == 14
    assert lawngrass.color == 'Bright green'


def test_add_different_product_types():
    smartphone = Smartphone(
        "Samsung S25",
        'Флагман',
        150000.124,
        2,
        96,
        'Basic',
        512,
        'Black'

    )

    lawngrass = LawnGrass(
        "Lawn Grass",
        'Трава высокая',
        2500,
        5,
        'Dutch',
        14,
        'Bright green'
    )

    with pytest.raises(TypeError):
        lawngrass + smartphone

def test_add_same_product_types():
    smartphone_1 = Smartphone(
        "Samsung S25",
        'Флагман',
        150000.124,
        2,
        96,
        'Basic',
        512,
        'Black'

    )

    smartphone_2 = Smartphone(
        "Samsung S21",
        'Прошлый флагман',
        50000.124,
        5,
        78,
        'Pro',
        128,
        'Silver'

    )
    assert smartphone_1 + smartphone_2 == (smartphone_1.price * smartphone_1.quantity) + (smartphone_2.price * smartphone_2.quantity)

def test_add_same_product_types_2():
    lawngrass_1 = LawnGrass(
        "Lawn Grass",
        'Трава высокая',
        2500,
        5,
        'Dutch',
        14,
        'Bright green'
    )

    lawngrass_2 = LawnGrass(
        "Lawn Grass",
        'Трава высокая',
        1500,
        1,
        'Dutch',
        14,
        'Bright green'
    )

    assert lawngrass_1 + lawngrass_2 == (lawngrass_1.price * lawngrass_1.quantity) + (lawngrass_2.price * lawngrass_2.quantity)



