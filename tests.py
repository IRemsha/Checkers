import unittest
import Window
from field import Field
from painter import Painter


class Tests(unittest.TestCase):
    def test_search_free_turn_cell(self):   # Проверка поиска (2 белые шашки)
        field = Field(4, "RU")
        field.field = \
            [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 1]]
        answer_list = [((1, 2), (0, 1)), ((1, 2), (2, 1)), ((3, 3), (2, 2))]
        self.assertEqual(Window.search_free_turn([], True, field), answer_list)

    # region СВОБОДНЫЕ ХОДЫ
    def test_free_turn_cell1(self):     # Проверка белой пешки 2 хода вперёд (не назад)
        field = Field(4, "RU")
        field.field = \
            [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 0]]
        answer_list = [((1, 2), (0, 1)), ((1, 2), (2, 1))]
        self.assertEqual(Window.free_turn_cell([], 1, 2, True, field), answer_list)

    def test_free_turn_cell2(self):     # Проверка черной шашки 2 хода назад
        field = Field(3, "RU")
        field.field = \
            [[0, 2, 0],
             [0, 0, 0],
             [0, 0, 0]]

        answer_list = [((1, 0), (2, 1)), ((1, 0), (0, 1))]
        self.assertEqual(Window.free_turn_cell([], 1, 0, False, field), answer_list)

    def test_free_turn_cell3(self):
        field = Field(4, "RU")
        field.field = \
            [[0, 0, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
        answer_list = [((2, 1), (1, 0)), ((2, 1), (3, 0))]
        self.assertEqual(Window.free_turn_cell([], 2, 1, True, field), answer_list)

    def test_free_turn_cell4(self):     # Проверка белой шашки 1 ход вперёд у стены
        field = Field(4, "RU")

        field.field = \
            [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 1]]
        answer_list = [((3, 3), (2, 2))]
        self.assertEqual(Window.free_turn_cell([], 3, 3, True, field), answer_list)

    def test_free_turn_cell5(self):     # Проверка белой шашки 2 хода вперёд
        field = Field(3, "RU")
        field.field = \
            [[0, 0, 0],
             [0, 0, 0],
             [0, 1, 0]]

        answer_list = [((1, 2), (0, 1)), ((1, 2), (2, 1))]
        self.assertEqual(Window.free_turn_cell([], 1, 2, True, field), answer_list)

    def test_free_turn_cell6(self):     # Проверка чёрной шашки два хода назад (не вперёд)
        field = Field(4, "RU")

        field.field = \
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 2, 0, 0],
         [0, 0, 0, 0]]

        answer_list = [((1, 2), (2, 3)), ((1, 2), (0, 3))]
        self.assertEqual(Window.free_turn_cell([], 1, 2, False, field), answer_list)

    def test_free_turn_cell7(self):     # Проверка белой шашки 1 ход вперёд у правой стены
        field = Field(4, "RU")

        field.field = \
            [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 1]]
        answer_list = [((3, 3), (2, 2))]
        self.assertEqual(Window.free_turn_cell([], 3, 3, True, field), answer_list)

    def test_free_turn_cell8(self):     # Проверка белой шашки 1 ход вперёд у левой стены
        field = Field(4, "RU")

        field.field = \
            [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [1, 0, 0, 0],
             [0, 0, 0, 0]]
        answer_list = [((0, 2), (1, 1))]
        self.assertEqual(Window.free_turn_cell([], 0, 2, True, field), answer_list)

    def test_free_turn_cell9(self):     # Проверка черной шашки 1 ход назад у левой стены
        field = Field(4, "RU")

        field.field = \
            [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [2, 0, 0, 0],
             [0, 0, 0, 0]]
        answer_list = [((0, 2), (1, 3))]
        self.assertEqual(Window.free_turn_cell([], 0, 2, False, field), answer_list)

    def test_free_turn_cell10(self):    # Проверка черной шашки 1 ход назад у правой стены
        field = Field(4, "RU")

        field.field = \
            [[0, 0, 0, 0],
             [0, 0, 0, 2],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
        answer_list = [((3, 1), (2, 2))]
        self.assertEqual(Window.free_turn_cell([], 3, 1, False, field), answer_list)

    def test_free_turn_cell11(self):    # Проверка черной шашки 0 ход назад у правой стены
        field = Field(4, "RU")

        field.field = \
            [[0, 0, 0, 0],
             [0, 0, 0, 2],
             [0, 0, 2, 0],
             [0, 0, 0, 0]]
        answer_list = []
        self.assertEqual(Window.free_turn_cell([], 3, 1, False, field), answer_list)

    def test_free_turn_cell12(self):     # Проверка черной шашки 0 ход назад у левой стены
        field = Field(4, "RU")

        field.field = \
            [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [2, 0, 0, 0],
             [0, 2, 0, 0]]
        answer_list = []
        self.assertEqual(Window.free_turn_cell([], 0, 2, False, field), answer_list)

    def test_free_turn_cell13(self):     # Проверка белой шашки 0 ход вперёд у левой стены
        field = Field(4, "RU")

        field.field = \
            [[0, 0, 0, 0],
             [0, 1, 0, 0],
             [1, 0, 0, 0],
             [0, 0, 0, 0]]
        answer_list = []
        self.assertEqual(Window.free_turn_cell([], 0, 2, True, field), answer_list)

    def test_free_turn_cell14(self):     # Проверка белой шашки 0 ход вперёд у правой стены
        field = Field(4, "RU")

        field.field = \
            [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1]]
        answer_list = []
        self.assertEqual(Window.free_turn_cell([], 3, 3, True, field), answer_list)


    #   endregion

    # region СВОБОДНЫЕ ХОДЫ КОРОЛЕЙ
    def test_free_turn_king1(self):
        field = Field(3, "RU")
        field.field = \
            [[0, 4, 0],
             [0, 0, 0],
             [0, 0, 0]]

        answer_list = [((1, 0), (0, 1)), ((1, 0), (2, 1))]
        self.assertEqual(Window.free_turn_king([], 1, 0, False, field), answer_list)

    def test_free_turn_king1_extra1(self):
        field = Field(2, "RU")

        field.field = \
            [[0, 4],
             [0, 0]]

        answer_list = [((1, 0), (0, 1))]
        self.assertEqual(Window.free_turn_king([], 1, 0, False, field), answer_list)

    def test_free_turn_king1_extra2(self):
        field = Field(3, "RU")
        field.field = \
            [[0, 0, 0],
             [0, 0, 0],
             [0, 4, 0]]

        answer_list = [((1, 2), (0, 1)), ((1, 2), (2, 1))]
        self.assertEqual(Window.free_turn_king([], 1, 2, False, field), answer_list)

    def test_free_turn_king1_extra3(self):
        field = Field(2, "RU")

        field.field = \
            [[0, 0],
             [4, 0]]

        answer_list = [((0, 1), (1, 0))]
        self.assertEqual(Window.free_turn_king([], 0, 1, False, field), answer_list)

    def test_free_turn_king2(self):
        field = Field(3, "RU")
        field.field = \
            [[0, 0, 0],
             [0, 0, 0],
             [0, 3, 0]]

        answer_list = [((1, 2), (0, 1)), ((1, 2), (2, 1))]
        self.assertEqual(Window.free_turn_king([], 1, 2, True, field), answer_list)

    def test_free_turn_king2_extra3(self):
        field = Field(2, "RU")

        field.field = \
            [[0, 0],
             [3, 0]]

        answer_list = [((0, 1), (1, 0))]
        self.assertEqual(Window.free_turn_king([], 0, 1, True, field), answer_list)

    def test_free_turn_king2_extra2(self):
        field = Field(3, "RU")
        field.field = \
            [[0, 3, 0],
             [0, 0, 0],
             [0, 0, 0]]

        answer_list = [((1, 0), (0, 1)), ((1, 0), (2, 1))]
        self.assertEqual(Window.free_turn_king([], 1, 0, True, field), answer_list)

    def test_free_turn_king2_extra1(self):
        field = Field(2, "RU")

        field.field = \
            [[0, 3],
             [0, 0]]

        answer_list = [((1, 0), (0, 1))]
        self.assertEqual(Window.free_turn_king([], 1, 0, True, field), answer_list)

    def test_free_turn_king3(self):
        field = Field(4, "RU")

        field.field = \
            [[0, 4, 0, 0],
             [2, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

        answer_list = [((1, 0), (2, 1)), ((1, 0), (3, 2))]
        self.assertEqual(Window.free_turn_king([], 1, 0, False, field), answer_list)

    def test_free_turn_king4(self):
        field = Field(4, "RU")

        field.field = \
            [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 3],
             [0, 0, 2, 0]]

        answer_list = [((3, 2), (2, 1)), ((3, 2), (1, 0))]
        self.assertEqual(Window.free_turn_king([], 3, 2, True, field), answer_list)

    def test_free_turn_king5(self):
        field = Field(4, "RU")

        field.field = \
            [[0, 0, 0, 0],
             [3, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

        answer_list = [((0, 1), (1, 0)), ((0, 1), (1, 2)), ((0, 1), (2, 3))]
        self.assertEqual(Window.free_turn_king([], 0, 1, True, field), answer_list)

    def test_free_turn_king6(self):
        field = Field(4, "RU")

        field.field = \
            [[0, 0, 0, 0],
             [3, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 0]]

        answer_list = [((0, 1), (1, 0))]
        self.assertEqual(Window.free_turn_king([], 0, 1, True, field), answer_list)

    def test_free_turn_king7(self):
        field = Field(4, "RU")

        field.field = \
            [[0, 1, 0, 0],
             [3, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 0]]

        answer_list = []
        self.assertEqual(Window.free_turn_king([], 0, 1, True, field), answer_list)

    def test_free_turn_king8(self):
        field = Field(4, "RU")

        field.field = \
            [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 4, 0, 0],
             [0, 0, 0, 0]]

        answer_list = [((1, 2), (0, 1)), ((1, 2), (0, 3)), ((1, 2), (2, 1)), ((1, 2), (3, 0)), ((1, 2), (2, 3))]
        self.assertEqual(Window.free_turn_king([], 1, 2, False, field), answer_list)

    def test_free_turn_king9(self):
        field = Field(4, "RU")

        field.field = \
            [[0, 0, 0, 0],
             [0, 0, 2, 0],
             [0, 4, 0, 0],
             [0, 0, 0, 0]]

        answer_list = [((1, 2), (0, 1)), ((1, 2), (0, 3)), ((1, 2), (2, 3))]
        self.assertEqual(Window.free_turn_king([], 1, 2, False, field), answer_list)

    def test_free_turn_king10(self):
        field = Field(4, "RU")

        field.field = \
            [[0, 0, 0, 0],
             [2, 0, 2, 0],
             [0, 4, 0, 0],
             [2, 0, 2, 0]]

        answer_list = []
        self.assertEqual(Window.free_turn_king([], 1, 2, False, field), answer_list)

    def test_free_turn_king11(self):
        field = Field(6, "RU")

        field.field = \
            [[0, 0, 0, 0, 0, 0],
             [2, 0, 2, 0, 0, 0],
             [0, 4, 0, 0, 0, 0],
             [2, 0, 0, 0, 0, 0],
             [0, 0, 0, 2, 0, 0],
             [0, 0, 0, 0, 0, 0]]

        answer_list = [((1, 2), (2, 3))]
        self.assertEqual(Window.free_turn_king([], 1, 2, False, field), answer_list)

    def test_free_turn_king12(self):
        field = Field(6, "RU")

        field.field = \
            [[0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 3, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 1]]

        answer_list = [((3, 3), (2, 2)), ((3, 3), (4, 4))]
        self.assertEqual(Window.free_turn_king([], 3, 3, True, field), answer_list)
    # endregion

    # region ОБЯЗАТЕЛЬНЫЕ ХОДЫ
    def test_must_turn_cell1(self):
        field = Field(4, "RU")
        field.field = \
               [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 2, 0],
                [0, 0, 0, 1]]
        answer_list = [((3, 3), (1, 1))]
        self.assertEqual(Window.must_turn_cell([], 3, 3, True, field), answer_list)

    def test_must_turn_cell2(self):
        field = Field(4, "RU")
        field.field = \
               [[0, 0, 0, 0],
                [0, 2, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0]]
        answer_list = [((2, 2), (0, 0))]
        self.assertEqual(Window.must_turn_cell([], 2, 2, True, field), answer_list)

    def test_must_turn_cell3(self):
        field = Field(6, "RU")
        field.field = \
            [[0, 0, 0, 0, 0, 0],
             [0, 0, 2, 0, 2, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 2, 0, 2, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]
        answer_list = [((3, 2), (1, 0)), ((3, 2), (1, 4)), ((3, 2), (5, 0)), ((3, 2), (5, 4))]
        self.assertEqual(Window.must_turn_cell([], 3, 2, True, field), answer_list)

    def test_must_turn_cell4(self):
        field = Field(6, "RU")
        field.field = \
            [[0, 2, 0, 0, 0, 2],
             [0, 0, 2, 0, 2, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 2, 0, 2, 0],
             [0, 2, 0, 0, 0, 2],
             [0, 0, 0, 0, 0, 0]]
        answer_list = []
        self.assertEqual(Window.must_turn_cell([], 3, 2, True, field), answer_list)

    def test_must_turn_cell5(self):
        field = Field(4, "RU")
        field.field = \
               [[0, 2, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
        answer_list = [((1, 0), (3, 2))]
        self.assertEqual(Window.must_turn_cell([], 1, 0, False, field), answer_list)

    def test_must_turn_cell6(self):
        field = Field(4, "RU")
        field.field = \
               [[0, 0, 0, 0],
                [0, 2, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0]]
        answer_list = [((1, 1), (3, 3))]
        self.assertEqual(Window.must_turn_cell([], 1, 1, False, field), answer_list)

    def test_must_turn_cell7(self):
        field = Field(6, "RU")
        field.field = \
            [[0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 1, 0],
             [0, 0, 0, 2, 0, 0],
             [0, 0, 1, 0, 1, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]
        answer_list = [((3, 2), (1, 0)), ((3, 2), (1, 4)), ((3, 2), (5, 0)), ((3, 2), (5, 4))]
        self.assertEqual(Window.must_turn_cell([], 3, 2, False, field), answer_list)

    def test_must_turn_cell8(self):
        field = Field(6, "RU")
        field.field = \
            [[0, 1, 0, 0, 0, 1],
             [0, 0, 1, 0, 1, 0],
             [0, 0, 0, 2, 0, 0],
             [0, 0, 1, 0, 1, 0],
             [0, 1, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0]]
        answer_list = []
        self.assertEqual(Window.must_turn_cell([], 3, 2, False, field), answer_list)

    def test_must_turn_cell9(self):
        field = Field(4, "RU")
        field.field = \
               [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 4, 0],
                [0, 0, 0, 1]]
        answer_list = [((3, 3), (1, 1))]
        self.assertEqual(Window.must_turn_cell([], 3, 3, True, field), answer_list)

    def test_must_turn_cell10(self):
        field = Field(4, "RU")
        field.field = \
            [[2, 0, 0, 0],
             [0, 3, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
        answer_list = [((0, 0), (2, 2))]
        self.assertEqual(Window.must_turn_cell([], 0, 0, False, field), answer_list)

    def test_must_turn_cell11(self):
        field = Field(6, "RU")
        field.field = \
            [[0, 0, 0, 0, 0, 0],
             [0, 0, 3, 0, 3, 0],
             [0, 0, 0, 2, 0, 0],
             [0, 0, 3, 0, 3, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]
        answer_list = [((3, 2), (1, 0)), ((3, 2), (1, 4)), ((3, 2), (5, 0)), ((3, 2), (5, 4))]
        self.assertEqual(Window.must_turn_cell([], 3, 2, False, field), answer_list)

    def test_must_turn_cell12(self):
        field = Field(6, "RU")
        field.field = \
            [[0, 4, 0, 0, 0, 4],
             [0, 0, 4, 0, 4, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 4, 0, 4, 0],
             [0, 4, 0, 0, 0, 4],
             [0, 0, 0, 0, 0, 0]]
        answer_list = []
        self.assertEqual(Window.must_turn_cell([], 3, 2, True, field), answer_list)

    def test_must_turn_cell13(self):
        field = Field(6, "RU")
        field.field = \
            [[0, 0, 0, 0, 0, 0],
             [0, 0, 4, 0, 4, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 4, 0, 4, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]
        answer_list = [((3, 2), (1, 0)), ((3, 2), (1, 4)), ((3, 2), (5, 0)), ((3, 2), (5, 4))]
        self.assertEqual(Window.must_turn_cell([], 3, 2, True, field), answer_list)

    def test_must_turn_cell14(self):
        field = Field(6, "RU")
        field.field = \
            [[0, 3, 0, 0, 0, 3],
             [0, 0, 3, 0, 3, 0],
             [0, 0, 0, 2, 0, 0],
             [0, 0, 3, 0, 3, 0],
             [0, 3, 0, 0, 0, 3],
             [0, 0, 0, 0, 0, 0]]
        answer_list = []
        self.assertEqual(Window.must_turn_cell([], 3, 2, False, field), answer_list)

    def test_must_turn_cell15(self):
        field = Field(4, "RU")
        field.field = \
               [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 2, 0, 0],
                [1, 0, 0, ]]
        answer_list = [((0, 3), (2, 1))]
        self.assertEqual(Window.must_turn_cell([], 0, 3, True, field), answer_list)

    def test_must_turn_cell16(self):
        field = Field(4, "RU")
        field.field = \
               [[0, 0, 0, 0],
                [0, 0, 0, 2],
                [0, 0, 1, 0],
                [0, 0, 0, ]]
        answer_list = [((3, 1), (1, 3))]
        self.assertEqual(Window.must_turn_cell([], 3, 1, False, field), answer_list)

    def test_must_turn_cell17(self):
        field = Field(6, "RU")
        field.field = \
            [[0, 0, 0, 0, 0, 0],
             [0, 0, 2, 0, 2, 0],
             [0, 0, 0, 2, 0, 0],
             [0, 0, 2, 0, 2, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]
        answer_list = []
        self.assertEqual(Window.must_turn_cell([], 3, 2, False, field), answer_list)

    def test_must_turn_cell18(self):
        field = Field(6, "RU")
        field.field = \
            [[0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 1, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 1, 0, 1, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]
        answer_list = []
        self.assertEqual(Window.must_turn_cell([], 3, 2, True, field), answer_list)

    def test_must_turn_cell119(self):
        field = Field(6, "RU")
        field.field = \
            [[0, 2, 0, 0, 0, 2],
             [0, 0, 1, 0, 1, 0],
             [0, 0, 0, 2, 0, 0],
             [0, 0, 1, 0, 1, 0],
             [0, 2, 0, 0, 0, 2],
             [0, 0, 0, 0, 0, 0]]
        answer_list = []
        self.assertEqual(Window.must_turn_cell([], 3, 2, False, field), answer_list)

    def test_must_turn_cell120(self):
        field = Field(6, "RU")
        field.field = \
            [[0, 1, 0, 0, 0, 1],
             [0, 0, 2, 0, 2, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 2, 0, 2, 0],
             [0, 1, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0]]
        answer_list = []
        self.assertEqual(Window.must_turn_cell([], 3, 2, True, field), answer_list)

    # endregion

    # region ОБЯЗАТЕЛЬНЫЕ ХОДЫ КОРОЛЕЙ
    def test_must_turn_king1(self):
        field = Field(4, "RU")
        field.field = \
            [[0, 0, 0, 3],
             [0, 0, 0, 0],
             [0, 2, 0, 0],
             [0, 0, 0, 0]]
        answer_list = [((3, 0), (0, 3))]
        self.assertEqual(Window.must_turn_king([], 3, 0, True, field), answer_list)

    def test_must_turn_king2(self):
        field = Field(4, "RU")
        field.field = \
            [[0, 0, 0, 0],
             [3, 0, 0, 0],
             [0, 2, 0, 0],
             [0, 0, 0, 0]]
        answer_list = [((0, 1), (2, 3))]
        self.assertEqual(Window.must_turn_king([], 0, 1, True, field), answer_list)

    def test_must_turn_king3(self):
        field = Field(4, "RU")
        field.field = \
            [[0, 0, 0, 0],
             [3, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 2, 0]]
        answer_list = []
        self.assertEqual(Window.must_turn_king([], 0, 1, True, field), answer_list)

    def test_must_turn_king4(self):
        field = Field(4, "RU")
        field.field = \
            [[0, 0, 0, 0],
             [4, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 0]]
        answer_list = [((0, 1), (2, 3))]
        self.assertEqual(Window.must_turn_king([], 0, 1, False, field), answer_list)

    def test_must_turn_king5(self):
        field = Field(4, "RU")
        field.field = \
            [[0, 0, 0, 4],
             [0, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 0]]
        answer_list = [((3, 0), (0, 3))]
        self.assertEqual(Window.must_turn_king([], 3, 0, False, field), answer_list)

    def test_must_turn_king6(self):
        field = Field(4, "RU")
        field.field = \
            [[0, 0, 0, 0],
             [4, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 1, 0]]
        answer_list = []
        self.assertEqual(Window.must_turn_king([], 0, 1, False, field), answer_list)

    def test_must_turn_king7(self):
        field = Field(6, "RU")
        field.field = \
            [[0, 4, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]
        answer_list = [((1, 0), (4, 3)), ((1, 0), (5, 4))]
        self.assertEqual(Window.must_turn_king([], 1, 0, False, field), answer_list)

    def test_must_turn_king8(self):
        field = Field(6, "RU")
        field.field = \
            [[0, 4, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]
        answer_list = [((1, 0), (5, 4))]
        self.assertEqual(Window.must_turn_king([], 1, 0, False, field), answer_list)
    # endregion


if __name__ == '__main__':
    unittest.main()
'''field.field = \
            [[0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]'''