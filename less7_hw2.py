# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
# пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


class Clothes:
    def __init__(self):
        self.square = 0

    def __str__(self):
        return self.square

    def __add__(self, other):
        return self.square + other.calc_square


class Coat(Clothes):
    def __init__(self, height):
        self.height = height
        self.square = 0

    @property
    def calc_square(self):
        self.square = 2 * self.height + 0.3
        return self.square


class Suit(Clothes):
    def __init__(self, size):
        self.size = size
        self.square = 0

    @property
    def calc_square(self):
        self.square = self.size/6.5 + 0.5
        return self.square


Square = Coat(48) + Suit(50)
print(Square)
