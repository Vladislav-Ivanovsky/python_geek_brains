# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class MatrixException(Exception):
    def __init__(self, text):
        self.__text = text


class Matrix:
    def __init__(self, matrix_data):
        self.__check(matrix_data)
        self.__matrix_data = matrix_data

    @property
    def matrix_data(self):
        return self.__matrix_data

    @property
    def rows(self):
        return len(self.__matrix_data)

    @property
    def columns(self):
        return len(self.__matrix_data[0])

    def __str__(self):
        matrix_string = ""
        for row in self.__matrix_data:
            matrix_string = matrix_string + str(row) + "\n"
        return matrix_string

    def __check(self, matrix_data=None, expected_rows=None, expected_columns=None):
        """ Проверяет, что из данных, переданных в matrix_data можно создать матрицу

        :param matrix_data: содержимое матрицы, должен быть список списков. Если = None, то просто берём данные
                            самой матрицы
        :param rows: если указан - то проверяется, что кол-во строк в матрице такое же как в атрибуте
        :param columns: если указан - то проверяется, что кол-во столбцов в матрице такое же как в атрибуте
        """
        matrix_data = self.__matrix_data if matrix_data is None else matrix_data
        if (type(matrix_data) is not list) or (len(matrix_data) == 0) or (type(matrix_data[0]) is not list):
            raise MatrixException("matrix_data не является списком списков")
        if (expected_rows is not None) and (len(matrix_data) != expected_rows):
            raise MatrixException(f"Количество строк в матрице не равно {expected_rows}")
        if (expected_columns is not None) and (len(matrix_data[0]) != expected_columns):
            raise MatrixException(f"Количество столбцов в матрице не равно {expected_columns}")

        # проверим следующее:
        # 1. все строки матрицы имеют ту же длину, что и первая
        # 2. все строки матрицы - это списки
        # 3. все элементы матрицы - это числа
        row0_columns_amount = len(matrix_data[0])
        for row in matrix_data:
            if type(row) is not list:
                raise MatrixException("matrix_data не является списком списков")
            if len(row) != row0_columns_amount:
                raise MatrixException("Неодинаковое число элементов в строках матрицы")
            for el in row:
                if type(el) not in (int, float):
                    raise MatrixException("Недопустимый тип элемента матрицы. Ожидается int или float")

    def __getitem__(self, index):
        return self.__matrix_data[index[0]][index[1]]

    def __add__(self, other):
        # сперва проверим, что матрица справа от оператора '+' совпадают по размеру c первой
        try:
            Matrix.__check(other, expected_rows=self.rows, expected_columns=self.columns)
        except Exception as ex:
            print(ex)
            return None

        matrix_sum = []
        matrix_row = []
        for row in range(0, self.rows):
            for column in range(0, self.columns):
                matrix_row.append(self[row, column] + other[row, column])
            matrix_sum.append(matrix_row)
            matrix_row = []
        return Matrix(matrix_sum)


try:
    m1 = None
    m2 = None
    m1 = Matrix([[2, 3, 4], [6, 7, 8]])
    m2 = Matrix([[10, 20, 30], [40, 50, 60]])
    m3 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
    m4 = Matrix([[100, 200, 300], [400, 500, 600], [700, 800, 900]])
    m5 = Matrix([[2, 3, 4], [6, 7, 8], ['a','b','c']])
except MatrixException as me:
    print(me)

print(f"Матрица 1:\n{m1}")
print(f"Матрица 2:\n{m2}")
print(f"Складываем матрицы 1 и 2:\n{m1 + m2}")
print("-------------------------------------")
print(f"Матрица 3:\n{m3}")
print(f"Матрица 4:\n{m4}")
print(f"Складываем матрицы 3 и 4:\n{m3 + m4}")




