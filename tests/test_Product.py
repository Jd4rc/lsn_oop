from unittest.mock import Mock

from src.Product import Product
import pytest

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
        'name': "New Product",
        'description': "456",
        'price': 170.0,
        'quantity': 4
    }

    product = Product.new_product(new_data, old_products)

    assert isinstance(product, Product)
    assert product.name == "New Product"
    assert product.description == "456"
    assert product.price == 170.0
    assert product.quantity == 4

def test_new_product_with_dublicates():
    old_product = Product(
        'Iphone 7',
        '32gb',
        150.0,
        8
    )

    products = [old_product]

    data = {
        'name': "Iphone 7",
        'price': 891.0,
        'quantity': 4
    }

    product = Product.new_product(data, products)

    assert product.price == 891.0
    assert product.quantity == 12


def test_new_product_with_less_price():
    old_product = Product(
        'Iphone 7',
        '32gb',
        150.0,
        8
    )

    products = [old_product]

    data = {
        'name': "Iphone 7",
        'price': 100.151,
        'quantity': 4
    }

    product = Product.new_product(data, products)

    assert product.price == 150.0
    assert product.quantity == 12


def test_new_product_with_invalid_price():
    data = {
        'name': "Iphone 7",
        'description': "123",
        'price': 0,
        'quantity': 4
    }


    with pytest.raises(ValueError):
        product = Product.new_product(data, [])


def test_price_setter_with_accept_lower_price(monkeypatch):
    mock_input = Mock(return_value="y")

    monkeypatch.setattr('builtins.input', mock_input)

    product = Product(
        'Iphone 7',
        '32gb',
        150.0,
        8
    )

    product.price = 100

    mock_input.assert_called_once()
    assert product.price == 100
    
