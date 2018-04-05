import random
from logger import logger
from enum import Enum


class Move(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Game:
    ENDGAME_TILE = 2048

    def __init__(self, size=4):
        self._size = size
        self.board = [0] * size ** 2
        self._score = 0
        self._duration = 0
        self._gen_tile()
        self.moves = {
            Move.UP: self.up,
            Move.DOWN: self.down,
            Move.LEFT: self.left,
            Move.RIGHT: self.right,
        }

    def move(self, move):
        board_changed, score = self.moves[move]()
        if board_changed:
            self._score += score
            self._new_turn()

    def left(self):
        logger.debug(f'board before left is {self._board_repr()}')
        cp_board = self.board[:]
        score = 0
        for i in range(self._size):
            row = self.board[i * self._size:(i + 1) * self._size]
            row, row_score = self._update(row)
            score += row_score
            self.board[i * self._size:(i + 1) * self._size] = row
        logger.debug(f'board after left is {self._board_repr()}')

        return cp_board != self.board, score

    def right(self):
        cp_board = self.board[:]
        score = 0
        for i in range(self._size):
            row = self.board[i * self._size:(i + 1) * self._size]
            row, row_score = self._update(reversed(row))
            score += row_score
            self.board[i * self._size:(i + 1) * self._size] = reversed(row)

        return cp_board != self.board, score

    def up(self):
        cp_board = self.board[:]
        score = 0
        for i in range(self._size):
            row = self.board[i::self._size]
            row, row_score = self._update(row)
            score += row_score
            self.board[i::self._size] = row

        return cp_board != self.board, score

    def down(self):
        cp_board = self.board[:]
        score = 0
        for i in range(self._size):
            row = self.board[i::self._size]
            row, row_score = self._update(reversed(row))
            score += row_score
            self.board[i::self._size] = reversed(row)

        return cp_board != self.board, score

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
        score = 0
        idx = 0
        while idx < len(updated_row) - 1:
            if updated_row[idx] == updated_row[idx + 1]:
                updated_row[idx] *= 2
                score += updated_row[idx]
                updated_row[idx + 1] = 0
            idx += 1
        updated_row = sorted(updated_row, key=lambda x: int(x > 0), reverse=True)

        return updated_row, score

    def _board_repr(self):
        res = '\n'
        for row in range(self._size):
            res += str(self.board[row * self._size:(row + 1) * self._size])
            res += '\n'
        return res

    @property
    def score(self):
        return self._score

    @property
    def duration(self):
        return self._duration

    def tile(self, x, y):
        return self.board[self._pos_to_n(x, y)]

    def finished(self):
        if self.ENDGAME_TILE in self.board:
            return True
        return False
        # board_orig = self.board[:]
        # moves = [self.up(), self.down(), self.left(), self.right()]
        # board_changed = any(moves)
        # self.board = board_orig
        # return not board_changed
