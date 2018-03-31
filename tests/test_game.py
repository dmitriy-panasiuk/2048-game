import pytest

from game import Game


def test_init():
    game = Game()

    assert len(list(filter(lambda x: x, game.board))) == 1


@pytest.mark.parametrize("input, expected", [
    (0, (0, 0)),
    (1, (0, 1)),
    (5, (1, 1)),
    (15, (3, 3)),
])
def test_n_to_pos(input, expected):
    game = Game()

    assert expected == game._n_to_pos(n=input)


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

    assert expected == game._n_to_pos(n=input)


@pytest.mark.parametrize("input, expected", [
    ((0, 0), 0),
    ((0, 1), 1),
    ((1, 0), 5),
    ((1, 3), 8),
    ((3, 4), 19),
    ((4, 4), 24),
])
def test_pos_to_n(input, expected):
    game = Game(size=5)

    assert expected == game._pos_to_n(*input)


@pytest.mark.parametrize("input, expected", [
    ((0, 0), 0),
    ((0, 1), 1),
    ((1, 0), 4),
    ((1, 3), 7),
    ((1, 1), 5),
    ((3, 3), 15),
])
def test_pos_to_n2(input, expected):
    game = Game()

    assert expected == game._pos_to_n(*input)


def test_gen_tile():
    game = Game()
    game._gen_tile()

    assert any(game.board)


def test_get_tile_multiple():
    game = Game()
    game._gen_tile()
    game._gen_tile()
    game._gen_tile()
    game._gen_tile()
    game._gen_tile()

    assert len(list(filter(lambda x: x, game.board))) == 6


@pytest.mark.parametrize("row, expected", [
    ([0, 0, 0, 2], [2, 0, 0, 0]),
    ([4, 0, 0, 2], [4, 2, 0, 0]),
    ([2, 4, 8, 16], [2, 4, 8, 16]),
    ([0, 2, 0, 0], [2, 0, 0, 0]),
    ([0, 2, 2, 0], [2, 2, 0, 0]),
    ([2, 0, 2, 2], [2, 2, 2, 0]),
])
def test_row_update(row, expected):
    game = Game()
    updated_row = game._update(row)

    assert expected == updated_row
