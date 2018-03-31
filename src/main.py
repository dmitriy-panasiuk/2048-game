import tkinter as tk

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
GRID_LEN = 4
BACKGROUND_COLOR = '#92877d'
BACKGROUND_COLOR_EMPTY = "#9e948a"
FONT = ("Verdana", 40, "bold")


class Application(tk.Frame):
    def __init__(self):
        super().__init__()
        self.pack()
        self.master.title('2048')
        self.init()
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


if __name__ == '__main__':
    app = Application()
