from tkinter import *
from tkinter import messagebox
import random
import time


# region Игровое_поле

def create_field(field1, n):
    for i in range(n):
        field1.append([])
        for j in range(n):
                if j % 2 == 0 and i % 2 != 0 and i < n/2-1:
                    field1[i].append(2)
                elif j % 2 == 0 and i % 2 != 0 and i > n-n/2:
                    field1[i].append(1)
                elif j % 2 == 0:
                    field1[i].append(0)
                elif j % 2 != 0 and i % 2 == 0 and i < n/2-1:
                    field1[i].append(2)
                elif j % 2 != 0 and i % 2 == 0 and i > n-n/2:
                    field1[i].append(1)
                else:
                    field1[i].append(0)
    return field1


size_field = 10
row_cell = size_field
im_cell_size = 50
size_window = size_field*im_cell_size
board_size = im_cell_size * row_cell


def create_new_board():
    field1 = []
    global field
    field = create_field(field1, size_field)
    '''field = [[0, 0, 0, 3],
             [0, 0, 0, 0],
             [0, 2, 0, 0],
             [0, 0, 0, 0]]'''

              # endregion

# region Отрисовка_доски


create_new_board()


def board_in_color(x_poz_1, y_poz_1, x_poz_2, y_poz_2):
    _ox = 0
    while _ox < board_size:
        _oy = 1 * im_cell_size
        while _oy < board_size:
            board.create_rectangle(_ox, _oy, _ox + im_cell_size, _oy + im_cell_size, fill="Gray")
            _oy += 2 * im_cell_size
        _ox += 2 * im_cell_size
    _ox = 1 * im_cell_size
    while _ox < board_size:
        _oy = 0
        while _oy < board_size:
            board.create_rectangle(_ox, _oy, _ox + im_cell_size, _oy + im_cell_size, fill="Gray")
            _oy += 2 * im_cell_size
        _ox += 2 * im_cell_size

    for y in range(size_field):  # рисуем стоячие пешки
        for x in range(size_field):
            z = field[y][x]
            if z:
                if (x_poz_1, y_poz_1) != (x, y):  # ЧТО ЭТО ЗА ХУЙНЯ? ЗАЧЕМ? ПОЧЕМУ?
                    board.create_image(x * im_cell_size, y * im_cell_size, anchor=NW, image=cell[z])


# endregion

# region Отрисовка_шашек


def cell_in_color():
    global cell
    global white_cell
    global black_cell
    white_cell = PhotoImage(file="images\\white_man.gif")
    black_cell = PhotoImage(file="images\\dark_man.gif")
    white_king = PhotoImage(file="images\\white_king.gif")
    black_king = PhotoImage(file="images\\dark_king.gif")
    cell = [0, white_cell, black_cell, white_king, black_king]

# endregion

# region Реализация_хода


def turn_player_vs_player(poz1_x, poz1_y, poz2_x, poz2_y):
    global whose_turn    # Ход != Белых = Ход Черных
    list_turn = list_turn_player(whose_turn)
    if list_turn:
        if ((poz1_x, poz1_y), (poz2_x, poz2_y)) in list_turn:
            if whose_turn:
                turn_while(poz1_x, poz1_y, poz2_x, poz2_y)
                whose_turn = False
                if not (poz2_x, poz2_y) in ((poz1_x+1, poz1_y+1),   # Может быть условие получше?
                                            (poz1_x+1, poz1_y-1),
                                            (poz1_x-1, poz1_y+1),
                                            (poz1_x-1, poz1_y-1)):
                    if double_jump([], poz2_x, poz2_y, whose_turn=True):
                        whose_turn = True
            else:
                turn_black(poz1_x, poz1_y, poz2_x, poz2_y)
                whose_turn = True
                if not (poz2_x, poz2_y) in ((poz1_x + 1, poz1_y + 1),   # Может быть условие получше?
                                            (poz1_x + 1, poz1_y - 1),
                                            (poz1_x - 1, poz1_y + 1),
                                            (poz1_x - 1, poz1_y - 1)):
                    if double_jump([], poz2_x, poz2_y, whose_turn=False):
                        whose_turn = False

            # turn_white_player = True
        else:
            # draw_failed_turn(poz1_x, poz1_y) пока не нужная подцветка
            messagebox.showerror(message='Вам необходимо совершить корректный ход!')
            # turn_white_player = True
    board.update()
    return whose_turn


def turn_player_vs_computer(poz1_x, poz1_y, poz2_x, poz2_y, color_player, player):
    global whose_turn  # Ход != Белых = Ход Черных
    list_turn = list_turn_player(color_player)

    if list_turn and color_player == whose_turn:
        if ((poz1_x, poz1_y), (poz2_x, poz2_y)) in list_turn:
            #messagebox.showerror(message='ХОД ЧЕЛОВЕКА!')
            if (color_player and player and whose_turn) or (not color_player and player and not whose_turn):
                if whose_turn:
                    turn_while(poz1_x, poz1_y, poz2_x, poz2_y)
                    whose_turn = False

                elif not whose_turn:
                    turn_black(poz1_x, poz1_y, poz2_x, poz2_y)
                    whose_turn = True
                if not (poz2_x, poz2_y) in ((poz1_x + 1, poz1_y + 1),  # Может быть условие получше?
                                            (poz1_x + 1, poz1_y - 1),
                                            (poz1_x - 1, poz1_y + 1),
                                            (poz1_x - 1, poz1_y - 1)):
                    if not whose_turn:
                        if double_jump([], poz2_x, poz2_y, whose_turn=True):
                            whose_turn = True
                    elif whose_turn:
                        if double_jump([], poz2_x, poz2_y, whose_turn=False):
                            whose_turn = False
            else:
                pass
        else:
            # draw_failed_turn(poz1_x, poz1_y) пока не нужная подцветка
            messagebox.showerror(message='Ходи нормально рукажоп!')
            # turn_white_player = True

    list_turn_2 = list_turn_computer(not color_player)

    if list_turn_2 and not color_player == whose_turn:
        if (not color_player and not player and whose_turn) \
                or not(not color_player and not player and not whose_turn):
            #messagebox.showerror(message='ХОД КОМПЬЮТЕРА !')
            (x1, y1), (x2, y2) = list_turn_2.pop(random.randint(0, len(list_turn_2)-1))
            if whose_turn:
                turn_while(x1, y1, x2, y2)
                whose_turn = False
            elif not whose_turn:
                turn_black(x1, y1, x2, y2)
                whose_turn = True
            if not (x2, y2) in ((x1 + 1, y1 + 1),  # Может быть условие получше?
                                        (x1 + 1, y1 - 1),
                                        (x1 - 1, y1 + 1),
                                        (x1 - 1, y1 - 1)):
                if not whose_turn:
                    if double_jump([], x2, y2, whose_turn=True):
                        whose_turn = True
                        turn_player_vs_computer(-1, -1, -1, -1,  color_player, player)
                elif whose_turn:
                    if double_jump([], x2, y2, whose_turn=False):
                        whose_turn = False
                        turn_player_vs_computer(-1, -1, -1, -1,  color_player, player)


    board.update()
    return whose_turn


def list_turn_player(whose_turn):
    list_turn = search_must_turn([], whose_turn)
    if not list_turn:
            list_turn = search_free_turn([], whose_turn)
    return list_turn


def list_turn_computer(color_computer):
    list_turn = search_must_turn([], color_computer)
    if not list_turn:
            list_turn = search_free_turn([], color_computer)
    return list_turn


def search_must_turn(list_turn, whose_turn):    # ВОЗМОЖНОСТЬ ДОБАВТЬ РАНЗНООБРАЗИЕ ДЛЯ ИСПАНСКИХ ШАШЕК
        for y in range(size_field):  # сканируем всё поле
            for x in range(size_field):
                if field[y][x] == 1 or field[y][x] == 2:
                    must_turn_cell(list_turn, x, y, whose_turn)
                if field[y][x] == 3 or field[y][x] == 4:
                    must_turn_king(list_turn, x, y, whose_turn)
        return list_turn


def double_jump(list_turn, x, y, whose_turn):
    if field[y][x] == 1 or field[y][x] == 2:
        must_turn_cell(list_turn, x, y, whose_turn)

    if field[y][x] == 3 or field[y][x] == 4:
        must_turn_king(list_turn, x, y, whose_turn)
    return list_turn


def must_turn_cell(list_turn, x0, y0, whose_turn):
    x, y, enemy_cell, enemy_king = 0, 0, 0, 0
    if field[y0][x0] == 1 and whose_turn:
        x, y = x0, y0
        enemy_cell, enemy_king = 2, 4
    elif field[y0][x0] == 2 and not whose_turn:
        x, y = x0, y0
        enemy_cell, enemy_king = 1, 3
    if enemy_king != 0:
        for ix, iy in (-1, -1), (-1, 1), (1, -1), (1, 1):
            if 0 <= y+iy+iy <= size_field-1 and 0 <= x+ix+ix <= size_field-1:
                if field[y+iy][x+ix] == enemy_cell or field[y+iy][x+ix] == enemy_king:
                    if field[y+iy+iy][x+ix+ix] == 0:
                        draw_must_turn(x + ix + ix, y + iy + iy)
                        list_turn.append(((x, y), (x + ix + ix, y + iy + iy)))


def must_turn_king(list_turn, x0, y0, whose_turn):
    x, y, enemy_cell, enemy_king, friendly_cell, friendly_king = 0, 0, 0, 0, 0, 0
    if field[y0][x0] == 3 and whose_turn:
        x, y = x0, y0
        enemy_cell, enemy_king = 2, 4
        friendly_cell, friendly_king = 1, 3
    elif field[y0][x0] == 4 and not whose_turn:
        x, y = x0, y0
        enemy_cell, enemy_king = 1, 3
        friendly_cell, friendly_king = 2, 4
    if enemy_king != 0:
        for ix, iy in (-1, -1), (-1, 1), (1, -1), (1, 1):
            osh = 0  # определение правильности хода
            for i in range(1, size_field):
                if 0 <= y + iy * i <= size_field-1 and 0 <= x + ix * i <= size_field-1:
                    if osh == 1:
                        draw_must_turn(x + ix + ix, y + iy + iy)
                        list_turn.append(((x, y), (x + ix * i, y + iy * i)))
                    if field[y + iy * i][x + ix * i] == enemy_cell or field[y + iy * i][x + ix * i] == enemy_cell:
                        osh += 1
                    if field[y + iy * i][x + ix * i] == friendly_cell \
                            or field[y + iy * i][x + ix * i] == friendly_cell\
                            or osh == 2:
                        if osh > 0:
                            list_turn.pop()
                        break


def search_free_turn(list_turn, whose_turn):
    for y in range(size_field):
        for x in range(size_field):
            if field[y][x] == 1 or field[y][x] == 2:
                free_turn_cell(list_turn, x, y, whose_turn)

            if field[y][x] == 3 or field[y][x] == 4:
                free_turn_king(list_turn, x, y, whose_turn)

    return list_turn


def free_turn_cell(list_turn, x0, y0, whose_turn):
    x, y, fork_left, fork_right = 0, 0, 0, 0
    if field[y0][x0] == 1 and whose_turn:
        x, y = x0, y0
        fork_left, fork_right = (-1, -1), (1, -1)
    elif field[y0][x0] == 2 and not whose_turn:
        x, y = x0, y0
        fork_left, fork_right = (1, 1), (-1, 1)
    if fork_left != 0:
        for ix, iy in fork_left, fork_right:
            if 0 <= y + iy <= size_field-1 and 0 <= x + ix <= size_field-1:
                if field[y + iy][x + ix] == 0:
                    list_turn.append(((x, y), (x + ix, y + iy)))


def free_turn_king(list_turn, x0, y0, whose_turn):
    x, y, friendly_cell, friendly_king = 0, 0, 0, 0
    if field[y0][x0] == 3 and whose_turn:
        x, y = x0, y0
        friendly_cell, friendly_king = 1, 3
    elif field[y0][x0] == 4 and not whose_turn:
        x, y = x0, y0
        friendly_cell, friendly_king = 2, 4
    if friendly_king != 0:
        for ix, iy in (-1, -1), (-1, 1), (1, -1), (1, 1):
            for i in range(1, size_field):
                if 0 <= y + iy * i <= size_field-1 and 0 <= x + ix * i <= size_field-1:
                    if field[y + iy * i][x + ix * i] == 0:
                        list_turn.append(((x, y), (x + ix * i, y + iy * i)))
                    if field[y + iy * i][x + ix * i] == friendly_cell or field[y + iy * i][x + ix * i] == friendly_king:
                        break


def turn_while(poz1_x, poz1_y, poz2_x, poz2_y):
        board_in_color(poz1_x, poz1_y, poz2_x, poz2_y)

        if poz2_y == 0:
            field[poz1_y][poz1_x] = 3

        field[poz2_y][poz2_x] = field[poz1_y][poz1_x]
        field[poz1_y][poz1_x] = 0

        kx = ky = 1
        if poz1_x < poz2_x:
            kx = -1
        if poz1_y < poz2_y:
            ky = -1

        x_poz, y_poz = poz2_x, poz2_y
        while (poz1_x != x_poz) or (poz1_y != y_poz):
            x_poz += kx
            y_poz += ky
            if field[y_poz][x_poz] != 0:
                field[y_poz][x_poz] = 0
                board_in_color(poz1_x, poz1_y, poz2_x, poz2_y)
        #messagebox.showerror(message='ХОД БЕЛЫХ !')
        board_in_color(poz1_x, poz1_y, poz2_x, poz2_y)

        check_winner()


def turn_black (poz1_x, poz1_y, poz2_x, poz2_y):
    board_in_color(poz1_x, poz1_y, poz2_x, poz2_y)

    if poz2_y == size_field-1:
        field[poz1_y][poz1_x] = 4
    field[poz2_y][poz2_x] = field[poz1_y][poz1_x]
    field[poz1_y][poz1_x] = 0

    kx = ky = -1
    if poz1_x < poz2_x:
        kx = 1
    if poz1_y < poz2_y:
        ky = 1

    x_poz, y_poz = poz2_x, poz2_y
    while (poz1_x != x_poz) or (poz1_y != y_poz):
        x_poz -= kx
        y_poz -= ky
        if field[y_poz][x_poz] != 0:
            field[y_poz][x_poz] = 0
            board_in_color(poz1_x, poz1_y, poz2_x, poz2_y)
    #messagebox.showerror(message='ХОД ЧЕРНЫХ !')
    board_in_color(poz1_x, poz1_y, poz2_x, poz2_y)
    check_winner()


def check_winner():
    flag = True
    for i in range(size_field):
        if 2 in field[i] or 4 in field[i]:
            flag = False
    if flag:
            messagebox.askyesno(message='Победили Белые!')

# endregion


# region Управление_от_игрока


def draw_must_turn(x, y):
    board.coords(cursor_4, x*50, y*50, x*50+50, y*50+50)


def draw_failed_turn(poz1_x, poz1_y):
    board.coords(cursor_3, poz1_x*50, poz1_y*50, poz1_x*50+50, poz1_y*50+50)


def position_cursor(event):
    if whose_turn:
        board.coords(cursor_1, event.x // 50 * 50, event.y // 50 * 50, event.x // 50 * 50 + 50, event.y // 50 * 50 + 50)
    else:
        board.coords(cursor_2, event.x // 50 * 50, event.y // 50 * 50, event.x // 50 * 50 + 50, event.y // 50 * 50 + 50)


def selection(event):
    global poz1_x, poz1_y, poz2_x, poz2_y

    x, y = event.x // 50, event.y // 50
    if field[y][x] != 0:  # Добавить проверку на Белого_Черёного_Короля.
        board.coords(selection, x * 50, y * 50, x * 50 + 50, y * 50 + 50)
        poz1_x, poz1_y = x, y
    else:
        if poz1_x != -1:
            poz2_x, poz2_y = x, y
            if turn_PVP:  # завести другую переменную с полем выбора Игрок_vs_Игрок или Игрок_vs_Компьютер.
                turn_player_vs_player(poz1_x, poz1_y, poz2_x, poz2_y)
            elif turn_PVE:
                turn_player_vs_computer(poz1_x, poz1_y, poz2_x, poz2_y, color_player=True, player=True)
            poz1_x = -1


if __name__ == '__main__':

    window_main = Tk()
    window_main.title('Demo_03')
    board = Canvas(window_main, width=size_window, height=size_window, bg='#FFFFFF')
    board.pack()

    window_option = Tk()
    window_option.title("Введите параметр игры")
    window_option.geometry("350x250")
    message = StringVar
    message_entry = Entry(textvariable=message)
    message_entry.place(relx=.10, rely=.20, anchor='c')

    turn_PVP = True
    turn_PVE = False
    whose_turn = True
    main_menu = Menu()
    main_menu.add_cascade(label="Edit")
    window_main.config(menu=main_menu)
    board.bind("<Motion>", position_cursor)
    board.bind("<Button>", selection)
    selection = board.create_rectangle(-1, -1, -1, -1, outline="green", width=5)
    cursor_1 = board.create_rectangle(-1, -1, -1, -1, outline="blue", width=5)
    cursor_2 = board.create_rectangle(-1, -1, -1, -1, outline="red", width=5)
    cursor_3 = board.create_rectangle(-1, -1, -1, -1, outline="black", width=5)
    cursor_4 = board.create_rectangle(-1, -1, -1, -1, outline="gold", width=5)

    # endregion

    # region Main
    cell_in_color()
    board_in_color(-1, -1, -1, -1)
    main_menu = Menu()
    main_menu.add_cascade(label="Edit")
    window_main.config(menu=main_menu)
    mainloop()

# endregion
