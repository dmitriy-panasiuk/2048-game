import random


class Game:

    def __init__(self, size=4):
        self._size = size
        self.board = [[0] * size for _ in range(size)]
        self._score = 0
        self._duration = 0

    def left(self):
        pass

    def right(self):
        pass

    def up(self):
        pass

    def down(self):
        pass

    def _new_turn(self):
        # Increase duration, generate new tile
        pass

    def _gen_tile(self):
        while True:
            n = random.randint(a=0, b=self._size**2-1)
            x, y = self._n_to_pos(n)
            if not self.board[x][y]:
                self.board[x][y] = 2
                return

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
