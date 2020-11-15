"""Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""


class Dress:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_coat(self):
        return self.size / 6.5 + 0.5

    def get_suit(self):
        return self.height * 2 + 0.3

    @property
    def area_cloths(self):
        return str(f'The total area of the fabric \n'
                   f' {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Dress):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.get_coat = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'he square of cloth to coat {self.get_coat}'


class Suit(Dress):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.get_suit = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'The square of cloth to suit {self.get_suit}'

coat = Coat(3, 6)
suit = Suit(2, 4)
print(coat)
print(suit)
print(suit.area_cloths)
print(coat.area_cloths)
print(suit.get_coat())
print(coat.get_suit())


# Вариант препадователя


# from abc import ABC, abstractmethod
#
# class Clothes(ABC):
#     def __init__(self, param):
#         self.param = param
#
#     @abstractmethod
#     def calculate(self):
#         pass
#
#
# class Coat(Clothes):
#
#     @property
#     def calculate(self):
#         return round((self.param / 6.5) + 0.5)
#
#
# class Suit(Clothes):
#
#     @property
#     def calculate(self):
#         return round((2 * self.param) + 0.3)
#
#
# coat = Coat(45)
# suit = Suit(170)
# print(coat.calculate)
# print(suit.calculate)
