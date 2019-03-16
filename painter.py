from tkinter import *
import time

from tkinter import messagebox


class Painter:
    def __init__(self, field, window, pixel):
        self.field = field
        self.window = window
        self.pixel = pixel
        self.white_cell = PhotoImage(file="images\\white_man.gif")
        self.black_cell = PhotoImage(file="images\\dark_man.gif")
        self.white_king = PhotoImage(file="images\\white_king.gif")
        self.black_king = PhotoImage(file="images\\dark_king.gif")
        self.pack = [0, self.white_cell, self.black_cell, self.white_king, self.black_king]
        self.size_window = self.field.size*self.pixel

    def main(self):
        """
        Главный метод рисовшика.
        :return:
        """
        self.board_in_color()

    def board_in_color(self):
        """
        Отрисовка доски.
        :return:
        """
        if self.field.mode == "POOL":
            self.window.create_rectangle(0, 0, self.size_window, self.size_window, fill="White")
        _ox = 0
        while _ox < self.size_window:
            _oy = 1 * self.pixel
            while _oy < self.size_window:
                self.window.create_rectangle(_ox, _oy, _ox + self.pixel, _oy + self.pixel, fill="Gray")
                _oy += 2 * self.pixel
            _ox += 2 * self.pixel

        _ox = 1 * self.pixel
        while _ox < self.size_window:
            _oy = 0
            while _oy < self.size_window:
                self.window.create_rectangle(_ox, _oy, _ox + self.pixel, _oy + self.pixel, fill="Gray")
                _oy += 2 * self.pixel
            _ox += 2 * self.pixel

        for y in range(self.field.size):  # рисуем стоячие пешки
            for x in range(self.field.size):
                z = self.field.field[y][x]
                if z:
                    if (-1, -1) != (x, y):
                        self.window.create_image(x * self.pixel, y * self.pixel, anchor=NW, image=self.pack[z])





