from abc import ABC
from abc import abstractmethod

from src.product import Product, InvalidQuantityError


class BasePrintable(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class Category(BasePrintable):
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """
        Инициализирует объект категории.

        Args:
            name: Название категории.
            description: Описание категории.
            products: Список продуктов категории.
        """
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __len__(self) -> int:
        """
        Возвращает количество продуктов в категории.

        Returns:
            Количество продуктов.
        """
        return len(self.__products)

    def __str__(self) -> str:
        """
        Возвращает строковое представление категории.

        Returns:
            Строка с названием категории и количеством продуктов.
        """
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def __iter__(self):
        """
        Возвращает итератор для перебора продуктов категории.

        Returns:
            Объект итератора CategoryIterator.
        """
        return CategoryIterator(self.__products)

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в категорию.

        Args:
            product: Объект класса Product.
        """

        if not isinstance(product, Product):
            raise TypeError(f"Ожидался Product, получен {type(product).__name__} ")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products_list(self):
        """Возвращает список продуктов категории."""
        return tuple(self.__products)

    @property
    def products(self):
        """возращает строковое представелние всех продуктов категории"""
        return "\n".join(str(product) for product in self.__products)

    @property
    def total_quantity(self) -> int:
        """
        Возвращает общее количество единиц товара в категории.

        Returns:
            Суммарное количество товаров.
        """
        return sum(product.quantity for product in self.__products)

    def middle_price(self):
        try:
            total_cost = sum(product.price * product.quantity for product in self.__products)
            return total_cost / self.total_quantity
        except ZeroDivisionError:
            return 0


class CategoryIterator:
    """
    Итератор для последовательного перебора продуктов категории.
    """

    def __init__(self, products: list[Product]) -> None:
        """
        Инициализирует итератор.

        Args:
            products: Список объектов Product для перебора.
        """
        self.products = products
        self.index = 0

    def __iter__(self):
        """
        Возвращает объект итератора.

        Returns:
            Текущий экземпляр итератора.
        """
        return self

    def __next__(self):
        """
        Возвращает следующий продукт из коллекции.

        Returns:
            Следующий объект Product.

        Raises:
            StopIteration: Если все продукты уже перебраны.
        """
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        raise StopIteration


class Order(BasePrintable):
    """Класс, представляющий заказ на покупку одного товара."""

    def __init__(self, product: Product, quantity: int) -> None:
        """
        Инициализирует заказ.

        Args:
            product: Купленный товар.
            quantity: Количество купленного товара.
        """

        if quantity <= 0:
            raise InvalidQuantityError(quantity)

        if not isinstance(product, Product):
            raise TypeError("Ожидался объект Product.")

        self.product = product
        self.quantity = quantity
        self.total_price = product.price * self.quantity

    def __str__(self) -> str:
        """
        Возвращает строковое представление заказа.

        Returns:
            Строка с информацией о товаре, количестве и итоговой стоимости.
        """
        return (
            f"Заказ с продуктом: {self.product.name}. "
            f"Количество: {self.quantity}, "
            f"на сумму: {self.total_price}"
        )
