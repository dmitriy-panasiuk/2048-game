import random


class Game:

    def __init__(self, size=4):
        self._size = size
        self.board = [0] * size**2
        self._score = 0
        self._duration = 0
        self._gen_tile()

    def left(self):
        pass

    def right(self):
        pass

    def up(self):
        pass

    def down(self):
        pass

    def _new_turn(self):
        self._duration += 1
        self._gen_tile()

    def _gen_tile(self):
        empty = [idx for idx, tile in enumerate(self.board) if not tile]
        r = random.choice(empty)
        self.board[r] = 2

    def _n_to_pos(self, n):
        return n // self._size, n % self._size

    def _pos_to_n(self, x, y):
        return x * self._size + y

    @property
    def score(self):
        return self._score

    @property
    def duration(self):
        return self._duration

    def tile(self, x, y):
        return self.board[self._pos_to_n(x, y)]
