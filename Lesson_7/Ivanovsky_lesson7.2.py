# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# - для пальто: (V/6.5 + 0.5)
# - для костюма (2*H + 0.3)
# Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property

from abc import ABC, abstractmethod


class Cloth(ABC):
    @property
    @abstractmethod
    def textile_size(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Coat(Cloth):
    def __init__(self, size):
        self.__size = size

    @property
    def textile_size(self):
        return self.__size / 6.5 + 0.5

    def __str__(self):
        return f"Костюм размером {self.__size}. Расход ткани: {self.textile_size:.2f}"


class Suit(Cloth):
    def __init__(self, growth):
        self.__growth = growth

    @property
    def textile_size(self):
        return self.__growth * 2 + 0.3

    def __str__(self):
        return f"Костюм размером {self.__growth}. Расход ткани: {self.textile_size:.2f}"


coat = Coat(size=42)
suit = Suit(growth=1.75)
print(coat)
print(suit)
