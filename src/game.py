import random


class Game:

    def __init__(self, size=4):
        self._size = size
        self.board = [0] * size**2
        self._score = 0
        self._duration = 0
        self._gen_tile()

    def left(self):
        for i in range(self._size):
            row = self.board[i*self._size:(i+1)*self._size]
            row = self._update(row)
        self._gen_tile()

    def right(self):
        self._gen_tile()

    def up(self):
        self._gen_tile()

    def down(self):
        self._gen_tile()

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

    def _update(self, row):
        updated_row = sorted(row, key=lambda x: int(x > 0), reverse=True)

        prev, prev_i = 0, 0
        for i, n in enumerate(updated_row[:]):
            if n != prev:
                updated_row[prev_i] = n
                prev = n
            else:
                updated_row[prev_i] += n
                prev = 0
                prev_i += 1
        return updated_row

    @property
    def score(self):
        return self._score

    @property
    def duration(self):
        return self._duration

    def tile(self, x, y):
        return self.board[self._pos_to_n(x, y)]
