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

    def __len__(self) -> int:
        return len(self.__products)

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def __iter__(self):
        return CategoryIterator(self.__products)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> list[str]:
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]

    @property
    def total_quantity(self) -> int:
        return sum(product.quantity for product in self.__products)


class CategoryIterator:
    def __init__(self, products: list) -> None:
        self.products = products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        raise StopIteration
