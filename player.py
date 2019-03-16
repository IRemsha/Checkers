'''from Window import *

class Player:
    def __init__(self, color):
        self.list_of_turn = []
        self.color = color

    def main(self):
        pass

    def list_turn_player(self, whose_turn):
        self.list_of_turn = search_must_turn(whose_turn)
        if not self.list_of_turn:
            self.list_of_turn = search_free_turn(whose_turn)
        return self.list_of_turn

    def search_must_turn(self, whose_turn):  # ВОЗМОЖНОСТЬ ДОБАВТЬ РАНЗНООБРАЗИЕ ДЛЯ ИСПАНСКИХ ШАШЕК
        for y in range(field.size):  # сканируем всё поле
            for x in range(field.size):
                if useful_field[y][x] == 1 or useful_field[y][x] == 2:
                    must_turn_cell(x, y, whose_turn)
                if useful_field[y][x] == 3 or useful_field[y][x] == 4:
                    must_turn_king(x, y, whose_turn)
        return self.list_of_turn

    def must_turn_cell(self, x0, y0, whose_turn):
        x, y, enemy_cell, enemy_king = 0, 0, 0, 0
        if useful_field[y0][x0] == 1 and whose_turn:
            x, y = x0, y0
            enemy_cell, enemy_king = 2, 4
        elif useful_field[y0][x0] == 2 and not whose_turn:
            x, y = x0, y0
            enemy_cell, enemy_king = 1, 3
        if enemy_king != 0:
            for ix, iy in (-1, -1), (-1, 1), (1, -1), (1, 1):
                if 0 <= y + iy + iy <= field.size - 1 and 0 <= x + ix + ix <= field.size - 1:
                    if useful_field[y + iy][x + ix] == enemy_cell or useful_field[y + iy][x + ix] == enemy_king:
                        if useful_field[y + iy + iy][x + ix + ix] == 0:
                            self.list_of_turn.append(((x, y), (x + ix + ix, y + iy + iy)))

    def must_turn_king(self, x0, y0, whose_turn):
        x, y, enemy_cell, enemy_king, friendly_cell, friendly_king = 0, 0, 0, 0, 0, 0
        if useful_field[y0][x0] == 3 and whose_turn:
            x, y = x0, y0
            enemy_cell, enemy_king = 2, 4
            friendly_cell, friendly_king = 1, 3
        elif useful_field[y0][x0] == 4 and not whose_turn:
            x, y = x0, y0
            enemy_cell, enemy_king = 1, 3
            friendly_cell, friendly_king = 2, 4
        if enemy_king != 0:
            for ix, iy in (-1, -1), (-1, 1), (1, -1), (1, 1):
                osh = 0  # определение правильности хода
                for i in range(1, field.size):
                    if 0 <= y + iy * i <= field.size - 1 and 0 <= x + ix * i <= field.size - 1:
                        if osh == 1:
                            self.list_of_turn.append(((x, y), (x + ix * i, y + iy * i)))
                        if useful_field[y + iy * i][x + ix * i] == enemy_cell or useful_field[y + iy * i][
                            x + ix * i] == enemy_cell:
                            osh += 1
                        if useful_field[y + iy * i][x + ix * i] == friendly_cell \
                                or useful_field[y + iy * i][x + ix * i] == friendly_cell \
                                or osh == 2:
                            if osh > 0:
                                self.list_of_turn.pop()
                            break

    def search_free_turn(self, whose_turn):
        for y in range(field.size):
            for x in range(field.size):
                if useful_field[y][x] == 1 or useful_field[y][x] == 2:
                    free_turn_cell(self.list_of_turn.append, x, y, whose_turn)

                if useful_field[y][x] == 3 or useful_field[y][x] == 4:
                    free_turn_king(x, y, whose_turn)

        return self.list_of_turn

    def free_turn_cell(self, x0, y0, whose_turn):
        x, y, fork_left, fork_right = 0, 0, 0, 0
        if useful_field[y0][x0] == 1 and whose_turn:
            x, y = x0, y0
            fork_left, fork_right = (-1, -1), (1, -1)
        elif useful_field[y0][x0] == 2 and not whose_turn:
            x, y = x0, y0
            fork_left, fork_right = (1, 1), (-1, 1)
        if fork_left != 0:
            for ix, iy in fork_left, fork_right:
                if 0 <= y + iy <= field.size - 1 and 0 <= x + ix <= field.size - 1:
                    if useful_field[y + iy][x + ix] == 0:
                        self.list_of_turn.append(((x, y), (x + ix, y + iy)))

    def free_turn_king(self, x0, y0, whose_turn):
        x, y, friendly_cell, friendly_king = 0, 0, 0, 0
        if useful_field[y0][x0] == 1 and whose_turn:
            x, y = x0, y0
            friendly_cell, friendly_king = 1, 3
        elif useful_field[y0][x0] == 2 and not whose_turn:
            x, y = x0, y0
            friendly_cell, friendly_king = 2, 4
        if friendly_king != 0:
            for ix, iy in (-1, -1), (-1, 1), (1, -1), (1, 1):
                for i in range(1, field.size):
                    if 0 <= y + iy * i <= field.size - 1 and 0 <= x + ix * i <= field.size - 1:
                        if useful_field[y + iy * i][x + ix * i] == 0:
                            self.list_of_turn.append(((x, y), (x + ix * i, y + iy * i)))
                        if useful_field[y + iy * i][x + ix * i] == friendly_cell or useful_field[y + iy * i][
                            x + ix * i] == friendly_king:
                            break
'''
