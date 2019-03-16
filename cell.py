from tkinter import *

class Cell:
    def __init__(self, color, rank):
        self.color = color
        self.rank = rank
        if self.rank == 2 and self.color == True:
            self.picture = PhotoImage(file="images\\white_man.gif")

    def cell_in_color(self):
        black_cell = PhotoImage(file="images\\dark_man.gif")
        white_king = PhotoImage(file="images\\white_king.gif")
        black_king = PhotoImage(file="images\\dark_king.gif")
        cell = [0, white_cell, black_cell, white_king, black_king]
