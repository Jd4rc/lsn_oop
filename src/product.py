class Product:
    """
    Класс, представляющий товар.

    Атрибуты:
        name: Наименование товара.
        description: Описание товара.
        price: Цена товара.
        quantity: Количество товара на складе.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализирует объект товара.

        Args:
            name: Наименование товара.
            description: Описание товара.
            price: Цена товара.
            quantity: Количество товара на складе.
        """
        self.__name = name
        self.__description = description
        self.price = price
        self.__quantity = quantity

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для отладки.

        Returns:
            Строковое представление товара.
        """
        return str(self)

    def __str__(self) -> str:
        """
        Возвращает строковое представление товара.

        Returns:
            Строка с названием, ценой и количеством товара.
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Возвращает суммарную стоимость двух товаров.

        Args:
            other: Другой объект Product.

        Returns:
            Суммарная стоимость товаров (цена × количество).

        Raises:
            TypeError:  Если операнды принадлежат разным классам.
        """
        if type(self) is not type(other):
            raise TypeError("Невозможно сложить объекты разных классов")

        return self.price * self.quantity + other.price * other.quantity

    @property
    def name(self) -> str:
        """
        Возвращает название товара.

        Returns:
            Название товара.
        """
        return self.__name

    @property
    def description(self) -> str:
        """
        Возвращает описание товара.

        Returns:
            Описание товара.
        """
        return self.__description

    @property
    def price(self) -> float:
        """
        Возвращает цену товара.

        Returns:
            Цена товара.
        """
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """
        Устанавливает цену товара.

        Проверяет, что цена положительная. При попытке понизить цену
        запрашивает подтверждение пользователя.

        Args:
            value: Новая цена товара.

        Raises:
            ValueError: Если цена меньше либо равна нулю.
        """
        if value <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")

        if hasattr(self, "_Product__price") and value < self.price:
            answer = input("Понизить цену: (y/n): ")

            if answer != "y":
                return

        self.__price = value

    @property
    def quantity(self) -> int:
        """
        Возвращает количество товара.

        Returns:
            Количество товара на складе.
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        """
        Устанавливает количество товара.

        Args:
            value: Новое количество товара.
        """
        self.__quantity = value

    @classmethod
    def new_product(cls, product_data: dict, products: list[Product] | None = None) -> Product:
        """
        Создает новый товар или обновляет существующий.

        Если товар с таким названием уже присутствует в списке,
        увеличивает его количество и оставляет максимальную цену.

        Args:
            product_data: Словарь с данными о товаре.
            products: Список существующих товаров.

        Returns:
            Новый или обновленный объект Product.
        """
        if products is None:
            products = []

        for product in products:
            if product.name == product_data["name"]:
                product.quantity += product_data["quantity"]
                product.price = max(product.price, product_data["price"])
                return product

        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )


class Smartphone(Product):
    """класс, представляющий смартфон"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """
        Инициализирует объект смартфона.

        Args:
            name: Название смартфона.
            description: Описание смартфона.
            price: Цена смартфона.
            quantity: Количество смартфонов на складе.
            efficiency: Производительность смартфона.
            model: Модель смартфона.
            memory: Объем памяти смартфона.
            color: Цвет смартфона.
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс, представляющий газонную траву."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """
        Инициализирует объект газонной травы.

        Args:
            name: Название газонной травы.
            description: Описание газонной травы.
            price: Цена газонной травы.
            quantity: Количество упаковок на складе.
            country: Страна-производитель.
            germination_period: Срок прорастания.
            color: Цвет травы.
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
