from src.Product import Product


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
