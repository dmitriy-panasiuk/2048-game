import tkinter as tk

from game import Game

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
GRID_LEN = 4
BACKGROUND_COLOR = '#92877d'
BACKGROUND_COLOR_EMPTY = "#9e948a"
FONT = ("Verdana", 40, "bold")

# Keys
KEY_UP_ALT = 'up'
KEY_DOWN_ALT = 'down'
KEY_LEFT_ALT = 'left'
KEY_RIGHT_ALT = 'right'

KEY_UP = 'w'
KEY_DOWN = 's'
KEY_LEFT = 'a'
KEY_RIGHT = 'd'


class Application(tk.Frame):

    def __init__(self):
        super().__init__()
        self.pack()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_press)
        self.init()
        self.game = Game()
        self.events = {
            KEY_UP: self.game.up, KEY_UP_ALT: self.game.up,
            KEY_DOWN: self.game.down, KEY_DOWN_ALT: self.game.down,
            KEY_LEFT: self.game.left, KEY_LEFT_ALT: self.game.left,
            KEY_RIGHT: self.game.right, KEY_RIGHT_ALT: self.game.right,
        }
        self.mainloop()

    def init(self):
        background = tk.Frame(master=self, width=WINDOW_WIDTH,
                              height=WINDOW_HEIGHT, bg=BACKGROUND_COLOR)
        # background.pack()
        background.grid()
        for i in range(GRID_LEN):
            for j in range(GRID_LEN):
                cell = tk.Frame(background, bg=BACKGROUND_COLOR_EMPTY,
                                width=WINDOW_WIDTH/GRID_LEN, height=WINDOW_HEIGHT/GRID_LEN)
                cell.grid(row=i, column=j, padx=1, pady=1)
                t = tk.Label(master=cell, text="", bg=BACKGROUND_COLOR_EMPTY,
                             justify=tk.CENTER, font=FONT, width=4, height=2)
                t.grid()

    def key_press(self, event):
        key_pressed = event.keysym
        print(key_pressed)


if __name__ == '__main__':
    app = Application()
