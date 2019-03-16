from tkinter import *
from painter import Painter
from field import Field
from tkinter import messagebox
import random
from tkinter import *
from tkinter import messagebox
import time


# region Реализация_хода


def turn_player_vs_player(poz1_x, poz1_y, poz2_x, poz2_y):
    """
    Реализация игры Игрок против Игрока.
    :param poz1_x:
    :param poz1_y:
    :param poz2_x:
    :param poz2_y:
    :return:
    """
    global whose_turn  # Ход != Белых = Ход Черных
    list_turn = list_turn_player(whose_turn)
    if list_turn:
        if ((poz1_x, poz1_y), (poz2_x, poz2_y)) in list_turn:
            if whose_turn:
                turn_while(poz1_x, poz1_y, poz2_x, poz2_y, field)
                whose_turn = False
                if not (poz2_x, poz2_y) in ((poz1_x + 1, poz1_y + 1),  # Может быть условие получше?
                                            (poz1_x + 1, poz1_y - 1),
                                            (poz1_x - 1, poz1_y + 1),
                                            (poz1_x - 1, poz1_y - 1)):
                    if double_jump([], poz2_x, poz2_y, field, whose_turn=True):
                        whose_turn = True
            else:
                turn_black(poz1_x, poz1_y, poz2_x, poz2_y, field)
                whose_turn = True
                if not (poz2_x, poz2_y) in ((poz1_x + 1, poz1_y + 1),  # Может быть условие получше?
                                            (poz1_x + 1, poz1_y - 1),
                                            (poz1_x - 1, poz1_y + 1),
                                            (poz1_x - 1, poz1_y - 1)):
                    if double_jump([], poz2_x, poz2_y, field, whose_turn=False):
                        whose_turn = False

            # turn_white_player = True
        else:
            # draw_failed_turn(poz1_x, poz1_y) пока не нужная подцветка
            messagebox.showerror(message='Вам необходимо совершить корректный ход!')
            # turn_white_player = True
    window.update()
    return whose_turn


def turn_player_vs_computer(poz1_x, poz1_y, poz2_x, poz2_y, color_player, player):
    """
    Реализация игры Игрок против Комптьютера.
    :param poz1_x:
    :param poz1_y:
    :param poz2_x:
    :param poz2_y:
    :param color_player:
    :param player:
    :return:
    """
    global whose_turn  # Ход != Белых = Ход Черных
    list_turn = list_turn_player(color_player)

    if list_turn and color_player == whose_turn:
        if ((poz1_x, poz1_y), (poz2_x, poz2_y)) in list_turn:
            # messagebox.showerror(message='ХОД ЧЕЛОВЕКА!')
            if (color_player and player and whose_turn) or (not color_player and player and not whose_turn):
                if whose_turn:
                    turn_while(poz1_x, poz1_y, poz2_x, poz2_y, field)
                    whose_turn = False

                elif not whose_turn:
                    turn_black(poz1_x, poz1_y, poz2_x, poz2_y, field)
                    whose_turn = True
                if not (poz2_x, poz2_y) in ((poz1_x + 1, poz1_y + 1),  # Может быть условие получше?
                                            (poz1_x + 1, poz1_y - 1),
                                            (poz1_x - 1, poz1_y + 1),
                                            (poz1_x - 1, poz1_y - 1)):
                    if not whose_turn:
                        if double_jump([], poz2_x, poz2_y, field, whose_turn=True):
                            whose_turn = True
                    elif whose_turn:
                        if double_jump([], poz2_x, poz2_y, field, whose_turn=False):
                            whose_turn = False
            else:
                pass
        else:
            # draw_failed_turn(poz1_x, poz1_y) пока не нужная подцветка
            messagebox.showerror(message='Не верный ход!')
            # turn_white_player = True

    list_turn_2 = list_turn_computer(not color_player)

    if list_turn_2 and not color_player == whose_turn:
        if (not color_player and not player and whose_turn) \
                or not (not color_player and not player and not whose_turn):
            # messagebox.showerror(message='ХОД КОМПЬЮТЕРА !')
            (x1, y1), (x2, y2) = list_turn_2.pop(random.randint(0, len(list_turn_2) - 1))
            if whose_turn:
                turn_while(x1, y1, x2, y2, field)
                whose_turn = False
            elif not whose_turn:
                turn_black(x1, y1, x2, y2, field)
                whose_turn = True
            if not (x2, y2) in ((x1 + 1, y1 + 1),  # Может быть условие получше?
                                (x1 + 1, y1 - 1),
                                (x1 - 1, y1 + 1),
                                (x1 - 1, y1 - 1)):
                if not whose_turn:
                    if double_jump([], x2, y2, field, whose_turn=True):
                        whose_turn = True
                        turn_player_vs_computer(-1, -1, -1, -1, color_player, player)
                elif whose_turn:
                    if double_jump([], x2, y2, field, whose_turn=False):
                        whose_turn = False
                        turn_player_vs_computer(-1, -1, -1, -1, color_player, player)

    window.update()
    return whose_turn


def list_turn_player(whose_turn):
    """
        Поиск списка ходов для игроков.
    :param whose_turn:
    :return:
    """
    list_turn = search_must_turn([], whose_turn, field)
    if not list_turn:
        list_turn = search_free_turn([], whose_turn, field)
    return list_turn


def list_turn_computer(color_computer):
    """
    Поиск списка ходов для компьютера.
    :param color_computer:
    :return:
    """
    list_turn = search_must_turn([], color_computer, field)
    if not list_turn:
        list_turn = search_free_turn([], color_computer, field)
    return list_turn


def search_must_turn(list_turn, whose_turn, field):  # ВОЗМОЖНОСТЬ ДОБАВТЬ РАНЗНООБРАЗИЕ ДЛЯ ИСПАНСКИХ ШАШЕК
    """
    Поиск обязательных ходов на поле.
    :param list_turn:
    :param whose_turn:
    :param field:
    :return:
    """
    for y in range(field.size):  # сканируем всё поле
        for x in range(field.size):
            if field.field[y][x] == 1 or field.field[y][x] == 2:
                must_turn_cell(list_turn, x, y, whose_turn, field)
            if field.field[y][x] == 3 or field.field[y][x] == 4:
                must_turn_king(list_turn, x, y, whose_turn, field)
    return list_turn


def double_jump(list_turn, x, y, field, whose_turn):
    """
    Мультипрыжок.
    :param list_turn:
    :param x:
    :param y:
    :param field:
    :param whose_turn:
    :return:
    """
    if field.field[y][x] == 1 or field.field[y][x] == 2:
        must_turn_cell(list_turn, x, y, whose_turn, field)

    if field.field[y][x] == 3 or field.field[y][x] == 4:
        must_turn_king(list_turn, x, y, whose_turn, field)
    return list_turn


def must_turn_cell(list_turn, x0, y0, whose_turn, field):
    """
        Поиск обязательных ходов за шашку.
    :param list_turn:
    :param x0:
    :param y0:
    :param whose_turn:
    :param field:
    :return:
    """
    x, y, enemy_cell, enemy_king = 0, 0, 0, 0
    if field.field[y0][x0] == 1 and whose_turn:
        x, y = x0, y0
        enemy_cell, enemy_king = 2, 4
    elif field.field[y0][x0] == 2 and not whose_turn:
        x, y = x0, y0
        enemy_cell, enemy_king = 1, 3
    if enemy_king != 0:
        for ix, iy in (-1, -1), (-1, 1), (1, -1), (1, 1):
            if 0 <= y + iy + iy <= field.size - 1 and 0 <= x + ix + ix <= field.size - 1:
                if field.field[y + iy][x + ix] == enemy_cell or field.field[y + iy][x + ix] == enemy_king \
                        and field.mode != "Cannibal":
                    if field.field[y + iy + iy][x + ix + ix] == 0:
                        list_turn.append(((x, y), (x + ix + ix, y + iy + iy)))
                elif field.field[y + iy][x + ix] != 0 and field.mode == "Cannibal":
                    if field.field[y + iy + iy][x + ix + ix] == 0:
                        list_turn.append(((x, y), (x + ix + ix, y + iy + iy)))
    return list_turn


def must_turn_king(list_turn, x0, y0, whose_turn, field):
    """
    Поиск обязательных ходов за дамку.
    :param list_turn:
    :param x0:
    :param y0:
    :param whose_turn:
    :param field:
    :return:
    """
    x, y, enemy_cell, enemy_king, friendly_cell, friendly_king = 0, 0, 0, 0, 0, 0
    if field.field[y0][x0] == 3 and whose_turn:
        x, y = x0, y0
        enemy_cell, enemy_king = 2, 4
        friendly_cell, friendly_king = 1, 3
    elif field.field[y0][x0] == 4 and not whose_turn:
        x, y = x0, y0
        enemy_cell, enemy_king = 1, 3
        friendly_cell, friendly_king = 2, 4
    if enemy_king != 0:
        for ix, iy in (-1, -1), (-1, 1), (1, -1), (1, 1):
            osh = 0  # определение правильности хода
            for i in range(1, field.size):
                if 0 <= y + iy * i <= field.size - 1 and 0 <= x + ix * i <= field.size - 1:
                    if osh == 1:
                        list_turn.append(((x, y), (x + ix * i, y + iy * i)))
                    if field.field[y + iy * i][x + ix * i] == enemy_cell \
                            or field.field[y + iy * i][x + ix * i] == enemy_cell:
                        osh += 1
                    if field.field[y + iy * i][x + ix * i] == friendly_cell \
                            or field.field[y + iy * i][x + ix * i] == friendly_cell \
                            or osh == 2:
                        if osh > 0:
                            list_turn.pop()
                        break
    return list_turn


def search_free_turn(list_turn, whose_turn, field):
    """
    Поиск свободных ходов на поле.
    :param list_turn:
    :param whose_turn:
    :param field:
    :return:
    """
    for y in range(field.size):
        for x in range(field.size):
            if field.field[y][x] == 1 or field.field[y][x] == 2:
                free_turn_cell(list_turn, x, y, whose_turn, field)

            if field.field[y][x] == 3 or field.field[y][x] == 4:
                free_turn_king(list_turn, x, y, whose_turn, field)

    return list_turn


def free_turn_cell(list_turn, x0, y0, whose_turn, field):
    """
    Происк свободного хода за шашку.
    :param list_turn:
    :param x0:
    :param y0:
    :param whose_turn:
    :param field:
    :return:
    """
    x, y, fork_left, fork_right = 0, 0, 0, 0
    if field.field[y0][x0] == 1 and whose_turn:
        x, y = x0, y0
        fork_left, fork_right = (-1, -1), (1, -1)
    elif field.field[y0][x0] == 2 and not whose_turn:
        x, y = x0, y0
        fork_left, fork_right = (1, 1), (-1, 1)
    if fork_left != 0:
        for ix, iy in fork_left, fork_right:
            if 0 <= y + iy <= field.size - 1 and 0 <= x + ix <= field.size - 1:
                if field.field[y + iy][x + ix] == 0:
                    list_turn.append(((x, y), (x + ix, y + iy)))
    return list_turn


def free_turn_king(list_turn, x0, y0, whose_turn, field):
    """
    Поиск свободного хода за дамку.
    :param list_turn:
    :param x0:
    :param y0:
    :param whose_turn:
    :param field:
    :return:
    """
    x, y, friendly_cell, friendly_king = 0, 0, 0, 0
    if field.field[y0][x0] == 3 and whose_turn:
        x, y = x0, y0
        friendly_cell, friendly_king = 1, 3
    elif field.field[y0][x0] == 4 and not whose_turn:
        x, y = x0, y0
        friendly_cell, friendly_king = 2, 4
    if friendly_king != 0:
        for ix, iy in (-1, -1), (-1, 1), (1, -1), (1, 1):
            for i in range(1, field.size):
                if 0 <= y + iy * i <= field.size - 1 and 0 <= x + ix * i <= field.size - 1:
                    if field.field[y + iy * i][x + ix * i] == 0:
                        list_turn.append(((x, y), (x + ix * i, y + iy * i)))
                    if field.field[y + iy * i][x + ix * i] == friendly_cell or \
                            field.field[y + iy * i][x + ix * i] == friendly_king:
                        break
    return list_turn


def turn_while(poz1_x, poz1_y, poz2_x, poz2_y, field):
    """
    Реализация хода за белые шашки.
    :param poz1_x:
    :param poz1_y:
    :param poz2_x:
    :param poz2_y:
    :param field:
    :return:
    """
    painter.board_in_color()

    if poz2_y == 0:
        field.field[poz1_y][poz1_x] = 3
    field.field[poz2_y][poz2_x] = field.field[poz1_y][poz1_x]
    field.field[poz1_y][poz1_x] = 0

    kx = ky = 1
    if poz1_x < poz2_x:
        kx = -1
    if poz1_y < poz2_y:
        ky = -1

    x_poz, y_poz = poz2_x, poz2_y
    while (poz1_x != x_poz) or (poz1_y != y_poz):
        x_poz += kx
        y_poz += ky
        if field.field[y_poz][x_poz] != 0:
            field.field[y_poz][x_poz] = 0
            painter.board_in_color()
    painter.board_in_color()

    check_winner(field)


def turn_black(poz1_x, poz1_y, poz2_x, poz2_y, field):
    """
    Реализация хода за чёрные шашки.
    :param poz1_x:
    :param poz1_y:
    :param poz2_x:
    :param poz2_y:
    :param field:
    :return:
    """
    painter.board_in_color()
    time.sleep(0.33)
    if poz2_y == field.size - 1:
        field.field[poz1_y][poz1_x] = 4
    field.field[poz2_y][poz2_x] = field.field[poz1_y][poz1_x]
    field.field[poz1_y][poz1_x] = 0

    kx = ky = -1
    if poz1_x < poz2_x:
        kx = 1
    if poz1_y < poz2_y:
        ky = 1

    x_poz, y_poz = poz2_x, poz2_y
    while (poz1_x != x_poz) or (poz1_y != y_poz):
        x_poz -= kx
        y_poz -= ky
        if field.field[y_poz][x_poz] != 0:
            field.field[y_poz][x_poz] = 0
            painter.board_in_color()
    # messagebox.showerror(message='ХОД ЧЕРНЫХ !')
    painter.board_in_color()
    check_winner(field)
    return field.field


def check_winner(field):
    """
    Проверка, на наличие победителя.
    :param field:
    :return:
    """
    flag_while = True
    flag_black = True
    for i in range(field.size):
        if 2 in field.field[i] or 4 in field.field[i]:
            flag_while = False
        elif 1 in field.field[i] or 3 in field.field[i]:
            flag_black = False
    if flag_while:
        messagebox.askyesno(message='Победили Белые!')
    elif flag_black:
        messagebox.askyesno(message='Победили Черных!')


# endregion


# region Управление_от_игрока

def position_cursor(event):
    """
    Подцветка выбранной клетки.
    :param event:
    :return:
    """
    window.coords(cursor_2,
                  event.x // painter.pixel * painter.pixel,
                  event.y // painter.pixel * painter.pixel,
                  event.x // painter.pixel * painter.pixel + painter.pixel,
                  event.y // painter.pixel * painter.pixel + painter.pixel)


def selection(event):
    """
    Выбирает клетку с шашке и делает вызывает метод, для совершения хода.
    :param event:
    :return:
    """
    global poz1_x, poz1_y, poz2_x, poz2_y

    x, y = event.x // painter.pixel, event.y // painter.pixel
    if field.field[y][x] != 0:
        window.coords(selection,
                      x * painter.pixel,
                      y * painter.pixel,
                      x * painter.pixel + painter.pixel,
                      y * painter.pixel + painter.pixel)
        poz1_x, poz1_y = x, y
    else:

        if poz1_x != -1:
            poz2_x, poz2_y = x, y
            if turn_PVP:  # завести другую переменную с полем выбора Игрок_vs_Игрок или Игрок_vs_Компьютер.
                turn_player_vs_player(poz1_x, poz1_y, poz2_x, poz2_y)
            elif turn_PVE:
                turn_player_vs_computer(poz1_x, poz1_y, poz2_x, poz2_y, color_player=False, player=True)
            poz1_x = -1


if __name__ == '__main__':
    turn_PVP = False
    turn_PVE = True
    whose_turn = True
    field = Field(16, "RU")
    field.main()
    root = Tk()
    root.title('TKcheckers')
    window = Canvas(root, width=field.size * 50, height=field.size * 50, bg='#FFFFFF')
    window.pack()
    main_menu = Menu()
    main_menu.add_cascade(label="Edit")
    cursor_2 = window.create_rectangle(-1, -1, -1, -1, outline="red", width=5)
    window.bind("<Motion>", position_cursor)
    window.bind("<Button>", selection)
    painter = Painter(field, window, 50)
    painter.main()

    root.config(menu=main_menu)

    mainloop()
