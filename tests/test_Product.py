from src.Product import Product

def test_product_initialization_1 (phone):
    assert phone.name == 'Pixel 5'
    assert phone.description == '123'
    assert phone.price == 1.1
    assert phone.quantity == 5

def test_product_initialization_2 ():
    pixel_10 = Product(
        'Pixel 10',
        '123',
        150.0,
        5
    )


    assert pixel_10.name == 'Pixel 10'
    assert pixel_10.description == '123'
    assert pixel_10.price == 150.0
    assert pixel_10.quantity == 5