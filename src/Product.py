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

    @classmethod
    def new_product(cls):
        ...