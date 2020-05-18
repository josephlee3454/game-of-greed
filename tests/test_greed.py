from game_of_greed.greed import GameLogic

# Tests for GameLogic:
## Tests for Roll dice
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
    actual = GameLogic.calculate_score((1,))
    expected = 100
    assert actual == expected


def test_single_five():
    actual = GameLogic.calculate_score((5,))
    expected = 50
    assert actual == expected


def test_two_fives():
    actual = GameLogic.calculate_score((5, 5, 6))
    expected = 100
    assert actual == expected


def test_two_ones():
    actual = GameLogic.calculate_score((1, 1))
    expected = 200
    assert actual == expected


def test_one_and_five():
    actual = GameLogic.calculate_score((1, 5))
    expected = 150
    assert actual == expected


def test_zilch():
    actual = GameLogic.calculate_score((2,))
    expected = 0
    assert actual == expected


def test_three_fives():
    actual = GameLogic.calculate_score((5, 5, 5, 2, 2, 3))
    expected = 500
    assert actual == expected


def test_three_ones():
    actual = GameLogic.calculate_score((1, 1, 1, 2, 3, 4))
    expected = 1000
    assert actual == expected


def test_three_ones_and_a_five():
    actual = GameLogic.calculate_score((1, 1, 1, 5))
    expected = 1050
    assert actual == expected


def test_straight():
    actual = GameLogic.calculate_score((1, 6, 3, 2, 5, 4))
    expected = 1500
    assert actual == expected


def test_three_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2))
    expected = 200
    assert actual == expected


def test_four_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2, 2))
    expected = 400
    assert actual == expected


def test_five_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2, 2, 2))
    expected = 600
    assert actual == expected


def test_six_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2, 2, 2, 2))
    expected = 800
    assert actual == expected


def test_six_ones():
    actual = GameLogic.calculate_score((1, 1, 1, 1, 1, 1))
    expected = 4000
    assert actual == expected


def test_three_pairs():
    actual = GameLogic.calculate_score((2, 2, 4, 4, 3, 3,))
    expected = 1500
    assert actual == expected
