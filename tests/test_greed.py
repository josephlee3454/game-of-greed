import pytest
from game_of_greed.greed import GameLogic, Banker

# Tests for class GameLogic:
# Tests for Roll dice
def test_roll_dice():
    game = GameLogic()
    actual = len(game.roll_dice(6))
    expected = 6
    assert actual == expected


def test_roll_dice_low():
    game = GameLogic()
    actual = len(game.roll_dice(2))
    expected = 2
    assert actual == expected


# Tests for Calculate Score
def test_single_one():
    actual, _ = GameLogic.calculate_score((1,), [1])
    expected = 100
    assert actual == expected


def test_single_five():
    actual, _ = GameLogic.calculate_score((5,), [1])
    expected = 50
    assert actual == expected


def test_two_fives():
    actual, _ = GameLogic.calculate_score((5, 5, 6), [1])
    expected = 100
    assert actual == expected


def test_two_ones():
    actual, _ = GameLogic.calculate_score((1, 1), [1])
    expected = 200
    assert actual == expected


def test_one_and_five():
    actual, _ = GameLogic.calculate_score((1, 5), [1])
    expected = 150
    assert actual == expected


def test_zilch():
    actual, _ = GameLogic.calculate_score((2,), [1])
    expected = 0
    assert actual == expected


def test_three_fives():
    actual, _ = GameLogic.calculate_score((5, 5, 5, 2, 2, 3), [1])
    expected = 500
    assert actual == expected


def test_three_ones():
    actual, _ = GameLogic.calculate_score((1, 1, 1, 2, 3, 4), [1])
    expected = 1000
    assert actual == expected


def test_three_ones_and_a_five():
    actual, _ = GameLogic.calculate_score((1, 1, 1, 5), [1])
    expected = 1050
    assert actual == expected


def test_straight():
    actual, _ = GameLogic.calculate_score((1, 6, 3, 2, 5, 4), [1])
    expected = 1500
    assert actual == expected


def test_three_of_a_kind():
    actual, _ = GameLogic.calculate_score((2, 2, 2), [1])
    expected = 200
    assert actual == expected


def test_four_of_a_kind():
    actual, _ = GameLogic.calculate_score((2, 2, 2, 2), [1])
    expected = 400
    assert actual == expected


def test_five_of_a_kind():
    actual, _ = GameLogic.calculate_score((2, 2, 2, 2, 2), [1])
    expected = 600
    assert actual == expected


def test_six_of_a_kind():
    actual, _ = GameLogic.calculate_score((2, 2, 2, 2, 2, 2), [1])
    expected = 800
    assert actual == expected


def test_six_ones():
    actual, _ = GameLogic.calculate_score((1, 1, 1, 1, 1, 1), [1])
    expected = 4000
    assert actual == expected


def test_three_pairs():
    actual, _ = GameLogic.calculate_score((2, 2, 4, 4, 3, 3,), [1])
    expected = 1500
    assert actual == expected


# Tests for class Banker
def test_new_banker_exists():
    assert Banker()


def test_new_banker():
    banker = Banker()
    assert banker.balance == 0
    assert banker.shelved == 0


def test_shelf():
    banker = Banker()
    banker.shelf(100)
    assert banker.shelved == 100
    assert banker.balance == 0


def test_deposit():
    banker = Banker()
    banker.shelf(100)
    output = banker.bank()
    banker.clear_shelf()
    assert output == 100
    assert banker.shelved == 0
    assert banker.balance == 100


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (tuple(), 0),
        ((1,), 100),
        ((1, 1), 200),
        ((1, 1, 1), 1000),
        ((1, 1, 1, 1), 2000),
        ((1, 1, 1, 1, 1), 3000),
        ((1, 1, 1, 1, 1, 1), 4000),
        ((2,), 0),
        ((2, 2), 0),
        ((2, 2, 2), 200),
        ((2, 2, 2, 2), 400),
        ((2, 2, 2, 2, 2), 600),
        ((2, 2, 2, 2, 2, 2), 800),
        ((3,), 0),
        ((3, 3), 0),
        ((3, 3, 3), 300),
        ((3, 3, 3, 3), 600),
        ((3, 3, 3, 3, 3), 900),
        ((3, 3, 3, 3, 3, 3), 1200),
        ((4,), 0),
        ((4, 4), 0),
        ((4, 4, 4), 400),
        ((4, 4, 4, 4), 800),
        ((4, 4, 4, 4, 4), 1200),
        ((4, 4, 4, 4, 4, 4), 1600),
        ((5,), 50),
        ((5, 5), 100),
        ((5, 5, 5), 500),
        ((5, 5, 5, 5), 1000),
        ((5, 5, 5, 5, 5), 1500),
        ((5, 5, 5, 5, 5, 5), 2000),
        ((6,), 0),
        ((6, 6), 0),
        ((6, 6, 6), 600),
        ((6, 6, 6, 6), 1200),
        ((6, 6, 6, 6, 6), 1800),
        ((6, 6, 6, 6, 6, 6), 2400),
        ((1, 2, 3, 4, 5, 6), 1500),
        ((2, 2, 3, 3, 4, 6), 0),
        ((2, 2, 3, 3, 6, 6), 1500),
    ],
)
def test_all(test_input, expected):
    actual, _ = GameLogic.calculate_score(test_input, [1])
    assert actual == expected
