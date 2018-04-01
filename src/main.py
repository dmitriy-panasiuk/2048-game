import tkinter as tk

from game import Game

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
GRID_LEN = 4
CELL_HEIGHT = WINDOW_HEIGHT/(GRID_LEN+1)
CELL_WIDTH = WINDOW_WIDTH/(GRID_LEN+1)
BACKGROUND_COLOR = '#92877d'
BACKGROUND_COLOR_EMPTY = "#9e948a"
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
        self.rows = []
        self.game = Game()
        self.events = {
            KEY_UP: self.game.up, KEY_UP_ALT: self.game.up,
            KEY_DOWN: self.game.down, KEY_DOWN_ALT: self.game.down,
            KEY_LEFT: self.game.left, KEY_LEFT_ALT: self.game.left,
            KEY_RIGHT: self.game.right, KEY_RIGHT_ALT: self.game.right,
        }
        self.init()
        self.update_grid()
        self.mainloop()

    def init(self):
        background = tk.Frame(master=self, width=WINDOW_WIDTH,
                              height=WINDOW_HEIGHT, bg=BACKGROUND_COLOR)
        # background.pack()
        background.grid()
        score_cell = tk.Frame(background, bg=BACKGROUND_COLOR_EMPTY,
                              width=CELL_WIDTH, height=CELL_HEIGHT)
        score_cell.grid(row=0, column=4, padx=1, pady=1)
        score = tk.Label(master=score_cell, text="0", bg=BACKGROUND_COLOR_EMPTY,
                         justify=tk.CENTER, font=FONT, width=4, height=2)
        score.grid()
        self.rows.append([None, None, None, score])
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

    def update_grid(self):
        for i in range(1, GRID_LEN+1):
            for j in range(GRID_LEN):
                v = self.game.tile(i-1, j)
                if not v:
                    self.rows[i][j].configure(text="", bg=BACKGROUND_COLOR_EMPTY)
                else:
                    self.rows[i][j].configure(text=v, bg=BACKGROUND_COLOR_DICT[v], fg=CELL_COLOR_DICT[v])
        self.update_idletasks()

    def key_press(self, event):
        key_pressed = event.keysym
        if key_pressed in self.events:
            self.events[key_pressed]()
            self.update_grid()


if __name__ == '__main__':
    app = Application()
