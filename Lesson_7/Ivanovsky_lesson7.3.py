# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# 1. сложение (__add__()) - объединение двух клеток. При этом число ячеек общей клетки должно равняться
#                           сумме ячеек исходных двух клеток,
# 2. вычитание (__sub__()) - участвуют две клетки. Операцию необходимо выполнять только если разность
#                            количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# 3. умножение (__mul__()) - создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
#                            количества ячеек этих двух клеток.
# 4. деление (__truediv__()) - создается общая клетка из двух. Число ячеек общей клетки определяется как
#                              целочисленное деление количества ячеек этих двух клеток
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
# количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

from itertools import *


class Cell:
    def __init__(self, size):
        if size < 0:
            print("Нельзя создать клетку с отрицательным размером")
            return
        self.__size = size

    @property
    def size(self):
        return self.__size

    def __add__(self, other):
        return Cell(self.size + other.size)

    def __sub__(self, other):
        if self.__size < other.size:
            print("Нельзя произвести вычитание. Размер уменьшаемой клетки меньше, чем вычитаемой")
            return None
        return Cell(self.size - other.size)

    def __mul__(self, other):
        return Cell(self.size * other.size)

    def __truediv__(self, other):
        return Cell(self.size // other.size)

    def make_order(self, cells_in_row):
        if self.__size == 0:
            return "Пустая клетка\n"
        if cells_in_row <= 0:
            print("Нельзя разложить клетку в отрицательное или нулевое количество рядов\n")
            return None
        if cells_in_row > self.__size:
            true_cells_in_row = self.__size
            full_rows = 1
        else:
            true_cells_in_row = cells_in_row
            full_rows = self.__size // cells_in_row
        cell_string = ""
        for rows in range(0, full_rows):
            cell_string = cell_string + "".join(repeat("*", true_cells_in_row)) + "\n"
        if true_cells_in_row == cells_in_row and self.__size % cells_in_row > 0:
            cell_string = cell_string + "".join(repeat("*", self.__size % cells_in_row))+"\n"
        return cell_string


c_incorrect1 = Cell(-10)
c1 = Cell(10)
c2 = Cell(20)
print(f"Первая клетка:\n{c1.make_order(5)}")
print(f"Вторая клетка:\n{c2.make_order(5)}")
print(f"Первая + вторая клетки:\n{(c1 + c2).make_order(10)}")
print(f"Первая - вторая клетки:\n{(c1 - c2)}\n")
print(f"Вторая - первая клетки:\n{(c2 - c1).make_order(4)}")
print(f"Первая * вторую клетки:\n{(c1 * c2).make_order(45)}")
print(f"Первая / вторую клетки:\n{(c1 / c2).make_order(10)}")
print(f"Вторая / первую клетки:\n{(c2 / c1).make_order(10)}")
