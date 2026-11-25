import pytest
from unittest.mock import MagicMock

from praktikum.burger import Burger


@pytest.fixture
def burger():
    """Пустой бургер."""
    return Burger()


@pytest.fixture
def bun():
    """Мок булочки с ценой 100 и именем 'Default bun'."""
    mock = MagicMock()
    mock.get_name.return_value = 'Default bun'
    mock.get_price.return_value = 100.0
    return mock

@pytest.fixture
def sauce():
    """Мок соуса."""
    mock = MagicMock()
    mock.get_name.return_value = 'Sauce'
    mock.get_type.return_value = 'SAUCE'
    mock.get_price.return_value = 20.0
    return mock


@pytest.fixture
def filling():
    """Мок начинки."""
    mock = MagicMock()
    mock.get_name.return_value = 'Filling'
    mock.get_type.return_value = 'FILLING'
    mock.get_price.return_value = 50.0
    return mock

@pytest.fixture
def extra():
    """Мок дополнительного ингредиента."""
    mock = MagicMock()
    mock.get_name.return_value = 'Extra'
    mock.get_type.return_value = 'FILLING'
    mock.get_price.return_value = 30.0
    return mock


@pytest.fixture
def filled_burger(burger, bun, sauce, filling):
    """Бургер с булочкой и двумя ингредиентами (для тестов, где не важна конкретная сборка)."""
    burger.set_buns(bun)
    burger.add_ingredient(sauce)
    burger.add_ingredient(filling)
    return burger
