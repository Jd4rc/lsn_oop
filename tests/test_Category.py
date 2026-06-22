def test_category_initialization(vegetable):
    assert vegetable.name == "Овощи"
    assert vegetable.description == "Свежие овощи"
    assert vegetable.products == []