from tkinter import *
from tkinter import messagebox


class Field:
    def __init__(self, size, mode):
        self.size = size
        self.field = []
        self.mode = mode

    def main(self):
        """
        Гланывый метод поля.
        :return:
        """
        if self.mode == "POOL":
            self.create_field_of_mod_pool()
        elif self.mode == "144":
            self.create_field_of_mod_144()
        elif self.mode == "RU" or self.mode == "Cannibal":
            self.create_field_of_mod_ru()
        else:
            self.create_field_of_mod_any()

    def create_field_of_mod_ru(self):
        """
        Создание доски по правилам "Русские шашки 8х8".
        :return:
        """
        self.size = 8
        for i in range(self.size):
            self.field.append([])
            for j in range(self.size):
                if j % 2 == 0 and i % 2 != 0 and i < self.size / 2 - 1:
                    self.field[i].append(2)
                elif j % 2 == 0 and i % 2 != 0 and i > self.size - self.size / 2:
                    self.field[i].append(1)
                elif j % 2 == 0:
                    self.field[i].append(0)
                elif j % 2 != 0 and i % 2 == 0 and i < self.size / 2 - 1:
                    self.field[i].append(2)
                elif j % 2 != 0 and i % 2 == 0 and i > self.size - self.size / 2:
                    self.field[i].append(1)
                else:
                    self.field[i].append(0)
        return self.field

    def create_field_of_mod_pool(self):
        """
        Создание доски по правилам "Full pool шашки 8х8".
        :return:
        """
        self.size = 8
        for i in range(self.size):
            self.field.append([])
            for j in range(self.size):
                if j % 2 == 0 and i % 2 == 0 and i < self.size / 2 - 1:
                    self.field[i].append(2)
                elif j % 2 == 0 and i % 2 == 0 and i > self.size - self.size / 2:
                    self.field[i].append(1)
                elif j % 2 == 0:
                    self.field[i].append(0)
                elif j % 2 != 0 and i % 2 != 0 and i < self.size / 2 - 1:
                    self.field[i].append(2)
                elif j % 2 != 0 and i % 2 != 0 and i > self.size - self.size / 2:
                    self.field[i].append(1)
                else:
                    self.field[i].append(0)
        return self.field

    def create_field_of_mod_144(self):
        """
        Создание доски по правилам "144 12х12".
        :return:
        """
        self.size=12
        for i in range(self.size):
            self.field.append([])
            for j in range(self.size):
                if j % 2 == 0 and i % 2 != 0 and i < self.size / 2 - 1:
                    self.field[i].append(2)
                elif j % 2 == 0 and i % 2 != 0 and i > self.size - self.size / 2:
                    self.field[i].append(1)
                elif j % 2 == 0:
                    self.field[i].append(0)
                elif j % 2 != 0 and i % 2 == 0 and i < self.size / 2 - 1:
                    self.field[i].append(2)
                elif j % 2 != 0 and i % 2 == 0 and i > self.size - self.size / 2:
                    self.field[i].append(1)
                else:
                    self.field[i].append(0)
        return self.field

    def create_field_of_mod_any(self):
        """
        Создание доски без определённых правил размером NxN.
        :return:
        """
        for i in range(self.size):
            self.field.append([])
            for j in range(self.size):
                if j % 2 == 0 and i % 2 != 0 and i < self.size / 2 - 1:
                    self.field[i].append(2)
                elif j % 2 == 0 and i % 2 != 0 and i > self.size - self.size / 2:
                    self.field[i].append(1)
                elif j % 2 == 0:
                    self.field[i].append(0)
                elif j % 2 != 0 and i % 2 == 0 and i < self.size / 2 - 1:
                    self.field[i].append(2)
                elif j % 2 != 0 and i % 2 == 0 and i > self.size - self.size / 2:
                    self.field[i].append(1)
                else:
                    self.field[i].append(0)
        return self.field