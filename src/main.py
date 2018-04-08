import tkinter as tk
from logger import logger

from game import Game, Move

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
GRID_LEN = 4
CELL_HEIGHT = WINDOW_HEIGHT/(GRID_LEN+1)
CELL_WIDTH = WINDOW_WIDTH/(GRID_LEN+1)
BACKGROUND_COLOR = '#92877d'
BACKGROUND_COLOR_EMPTY = "#9e948a"
SCORE_BACKGROUND_COLOR = 'sienna1'
SCORE_COLOR = 'snow'
FONT = ("Verdana", 40, "bold")

# Keys
KEY_UP_ALT = 'Up'
KEY_DOWN_ALT = 'Down'
KEY_LEFT_ALT = 'Left'
KEY_RIGHT_ALT = 'Right'

KEY_UP = 'w'
KEY_DOWN = 's'
KEY_LEFT = 'a'
KEY_RIGHT = 'd'

BACKGROUND_COLOR_DICT = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563",
                         32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61",
                         512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"}
CELL_COLOR_DICT = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
                   32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", 256: "#f9f6f2",
                   512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"}


class Application(tk.Frame):

    def __init__(self):
        super().__init__()
        self.pack()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_press)
        self.events = {
            KEY_UP: Move.UP, KEY_UP_ALT: Move.UP,
            KEY_DOWN: Move.DOWN, KEY_DOWN_ALT: Move.DOWN,
            KEY_LEFT: Move.LEFT, KEY_LEFT_ALT: Move.LEFT,
            KEY_RIGHT: Move.RIGHT, KEY_RIGHT_ALT: Move.RIGHT,
        }
        self.rows = []
        self.game = Game()
        self.score = None
        self.init()
        self.mainloop()

    def init(self):
        self.rows = []
        self.game = Game()
        self.score = None
        background = tk.Frame(master=self, width=WINDOW_WIDTH,
                              height=WINDOW_HEIGHT, bg=BACKGROUND_COLOR)
        background.grid()
        score_cell = tk.Frame(background, bg=BACKGROUND_COLOR_EMPTY,
                              width=CELL_WIDTH, height=CELL_HEIGHT)
        score_cell.grid(row=0, column=GRID_LEN-1, padx=1, pady=1)
        score = tk.Label(master=score_cell, text="0", bg=SCORE_BACKGROUND_COLOR, fg=SCORE_COLOR,
                         justify=tk.CENTER, font=FONT, width=4, height=2)
        score.grid()
        self.score = score
        for i in range(1, GRID_LEN+1):
            row = []
            for j in range(GRID_LEN):
                cell = tk.Frame(background, bg=BACKGROUND_COLOR_EMPTY,
                                width=CELL_WIDTH, height=CELL_HEIGHT)
                cell.grid(row=i, column=j, padx=1, pady=1)
                t = tk.Label(master=cell, text="", bg=BACKGROUND_COLOR_EMPTY,
                             justify=tk.CENTER, font=FONT, width=4, height=2)
                t.grid()
                row.append(t)
            self.rows.append(row)
        self.update_grid()

    def update_grid(self):
        self.score.configure(text=self.game.score)
        for i in range(GRID_LEN):
            for j in range(GRID_LEN):
                v = self.game.tile(i, j)
                if not v:
                    self.rows[i][j].configure(text="", bg=BACKGROUND_COLOR_EMPTY)
                else:
                    self.rows[i][j].configure(text=v, bg=BACKGROUND_COLOR_DICT[v], fg=CELL_COLOR_DICT[v])
        self.update_idletasks()

    def key_press(self, event):
        key_pressed = event.keysym
        logger.debug(f'Key pressed {key_pressed}')
        if key_pressed in self.events:
            self.game.move(self.events[key_pressed])
            self.update_grid()
        if self.game.finished():
            self.end_game()
            self.game = Game()
            self.update_grid()

    def end_game(self):
        toplevel = tk.Toplevel()
        label1 = tk.Label(toplevel, text=f'Game finished, you score is {self.game.score}', height=10, width=25)
        label1.pack()


if __name__ == '__main__':
    app = Application()
