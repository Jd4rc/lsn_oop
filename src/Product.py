from itertools import product


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(
            self, name: str,
            description: str,
            price: float,
            quantity: int
    ) -> None:
        self.__name = name
        self.__description = description
        self.__price = price
        self.__quantity = quantity

    def __repr__(self) -> str:
        return (
            f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт'
        )

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def price(self) -> float:
        return self.__price

    @property
    def quantity(self) -> int:
        return self.__quantity

    @price.setter
    def price(self, price: float) -> None:
        self.__price = price

    @quantity.setter
    def quantity(self, quantity: int) -> None:
        self.__quantity = quantity

    @classmethod
    def new_product(
            cls,
            product_data: dict,
            products: list[Product]
    ) -> Product:

        for product in products:
            if product.name == product_data['name']:
                product.quantity += product_data['quantity']
                product.price = max(product.price, product_data['price'])
                return product

        return cls(
            product_data['name'],
            product_data['description'],
            product_data['price'],
            product_data['quantity']
        )