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
            self.board[i * self._size:(i + 1) * self._size] = row
        self._new_turn()

    def right(self):
        for i in range(self._size):
            row = self.board[i*self._size:(i+1)*self._size]
            row = self._update(reversed(row))
            self.board[i * self._size:(i + 1) * self._size] = reversed(row)
        self._new_turn()

    def up(self):
        for i in range(self._size):
            row = self.board[i::self._size]
            row = self._update(row)
            self.board[i::self._size] = row
        self._new_turn()

    def down(self):
        for i in range(self._size):
            row = self.board[i::self._size]
            row = self._update(reversed(row))
            self.board[i::self._size] = reversed(row)
        self._new_turn()

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
        idx = 0
        while idx < len(updated_row)-1:
            if updated_row[idx] == updated_row[idx+1]:
                updated_row[idx] *= 2
                updated_row[idx+1] = 0
            idx += 1
        updated_row = sorted(updated_row, key=lambda x: int(x > 0), reverse=True)

        return updated_row

    @property
    def score(self):
        return self._score

    @property
    def duration(self):
        return self._duration

    def tile(self, x, y):
        return self.board[self._pos_to_n(x, y)]
