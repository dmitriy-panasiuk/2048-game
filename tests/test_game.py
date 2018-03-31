import pytest

from game import Game


def test_init():
    game = Game()

    assert game.board == [[0] * 4 for _ in range(4)]


@pytest.mark.parametrize("input, expected", [
    (0, (0, 0)),
    (1, (0, 1)),
    (5, (1, 1)),
    (15, (3, 3)),
])
def test_n_to_pos(input, expected):
    game = Game()

    assert game._n_to_pos(n=input) == expected


@pytest.mark.parametrize("input, expected", [
    (0, (0, 0)),
    (1, (0, 1)),
    (5, (1, 0)),
    (8, (1, 3)),
    (19, (3, 4)),
    (24, (4, 4)),
])
def test_n_to_pos2(input, expected):
    game = Game(size=5)

    assert game._n_to_pos(n=input) == expected
