from src.Product import Product

def test_product_initialization (phone):
    assert phone.name == 'Pixel 5'
    assert phone.description == '123'
    assert phone.price == 1.1
    assert phone.quantity == 5