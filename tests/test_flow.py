import pytest
from tests.flow.flo import Flo


def test_wanna_play():
    Flo.test("tests/flow/wanna_play.txt")


def test_do_wanna_play_then_quit():
    Flo.test("tests/flow/do_wanna_play_then_quit.txt")


def test_bank_one_roll_then_quit():
    Flo.test("tests/flow/bank_one_roll_then_quit.txt")


def test_bank_first_for_two_rounds():
    Flo.test("tests/flow/bank_first_for_two_rounds.txt")


def test_cheat_and_fix():
    Flo.test("tests/flow/cheat_and_fix.txt")