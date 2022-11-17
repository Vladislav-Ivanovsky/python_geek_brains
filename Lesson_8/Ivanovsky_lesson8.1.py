# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, day=0, month=0, year=0):
        self.__day = day
        self.__month = month
        self.__year = year

    @staticmethod
    def is_valid(string):
        days_in_month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        day, month, year = map(int, string.split("-"))
        return (month <= 12) and (day <= days_in_month[month]) and (year > 0 and year < 10000)

    @classmethod
    def from_string(cls, string):
        if cls.is_valid(string):
            day, month, year = map(int, string.split("-"))
            return Date(day=day, month=month, year=year)
        else:
            return None


print(f"Верна ли дата <31-02-2022>: {Date.is_valid('31-02-2022')}")
print(f"Объект Date <31-02-2022>: {Date.from_string('31-02-2022')}")
print(f"Верна ли дата <001-12-2022>: {Date.is_valid('001-12-2022')}")
print(f"Объект Date <001-12-2022>: {Date.from_string('001-12-2022').__dict__}")
print(f"Верна ли дата <01-01-18900>: {Date.is_valid('01-01-18900')}")
print(f"Объект Date <01-01-18900>: {Date.from_string('01-01-18900')}")
print(f"Верна ли дата <07-11-1917>: {Date.is_valid('07-11-1917')}")
print(f"Объект Date <07-11-1917>: {Date.from_string('07-11-1917').__dict__}")