class InvalidQuantityError(Exception):
    """Исключение, возникающее при недопустимом количестве товара."""

    def __init__(self, quantity: int) -> None:
        self.quantity = quantity

        super().__init__(f"Недопустимое количество товара: {quantity}")