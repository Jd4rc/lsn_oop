from src.Product import Product

class Category:
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)


    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> list[str]:
        return [
            f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.'
            for product in self.__products
        ]

