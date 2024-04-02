import pytest

from game.game_rules import play_game


def preset_feeder(inputs: list[int]):
    for elem in inputs:
        yield elem


def test_vertical_win():
    assert play_game(preset_feeder([1, 2, 1, 3, 1, 5, 1, 5, 3, 6])) == 'A'


def test_horizontal_win():
    assert play_game(preset_feeder([1, 5, 2, 5, 3, 5, 4, 5])) == 'A'


def test_diagonal_win_bottom_up():
    assert play_game(preset_feeder([1, 2, 2, 3, 3, 1, 3, 4, 4, 4, 4])) == 'A'


def test_diagonal_win_top_down():
    assert play_game(preset_feeder([4, 4, 4, 4, 3, 1, 3, 3, 2, 2, 1])) == 'B'


def test_no_win():
    assert play_game(preset_feeder([1, 1])) is None


def test_illegal_move():
    with pytest.raises(Exception):
        assert play_game(preset_feeder([6, 1, 1])) is None
