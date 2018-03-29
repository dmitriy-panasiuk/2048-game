class Game:

    def __init__(self, size=4):
        self.board = [[0] * 4 for _ in range(size)]
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

    @property
    def score(self):
        return self._score

    @property
    def duration(self):
        return self._duration
