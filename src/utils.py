import json
from pathlib import Path

from src.Category import Category
from src.Product import Product


def load_data(
    path: str | Path,
) -> list[Category]:
    with open(path, "r", encoding="UTF-8") as f:
        data = json.load(f)

    categories = []

    for category_data in data:
        products = []

        for product_data in category_data["products"]:
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"],
            )

            products.append(product)

        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products,
        )
        categories.append(category)

    return categories
