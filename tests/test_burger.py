import pytest

class TestBurger:
    """Тесты класса Burger."""

    def test_initial_state(self, burger):
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun is bun

    def test_add_ingredients(self, burger, sauce, filling):
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        assert burger.ingredients == [sauce, filling]

    def test_remove_ingredient(self, burger, sauce, filling):
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        burger.remove_ingredient(0)
        assert burger.ingredients == [filling]

    @pytest.mark.parametrize('index', [-1, 5])
    def test_remove_invalid_index(self, burger, index):
        with pytest.raises(IndexError):
            burger.remove_ingredient(index)

    @pytest.mark.parametrize(
        'from_idx, to_idx, expected',
        [
            (0, 2, [1, 2, 0]),  
            (2, 0, [2, 0, 1]),  
            (1, 1, [0, 1, 2]),  
        ],
    )
    def test_move_ingredient(self, burger, sauce, filling, extra, from_idx, to_idx, expected):
        ingredients = [sauce, filling, extra]
        for ing in ingredients:
            burger.add_ingredient(ing)

        burger.move_ingredient(from_idx, to_idx)
        assert burger.ingredients == [ingredients[i] for i in expected]
    
    def test_price_only_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.get_price() == 200.0

    def test_price_with_ingredients(self, burger, bun, sauce, filling):
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        assert burger.get_price() == 270.0

    def test_receipt_format(self, burger, bun, sauce, filling):
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        receipt = burger.get_receipt()
        assert '(==== Default bun ====)' in receipt
        assert '= sauce Sauce =' in receipt
        assert '= filling Filling =' in receipt
        assert 'Price: 270.0' in receipt
        