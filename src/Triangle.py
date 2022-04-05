from src.Figure import Figure
from math import sqrt


class Triangle(Figure):
    def __init__(self, side_base, side_a, side_b):
        super().__init__()
        if side_base <= 0 or side_a <= 0 or side_b <= 0:
            raise ValueError("Сторона не может быть <= 0")
        elif ((side_base + side_a) < side_b) or ((side_base + side_b) < side_a) or ((side_a + side_b) < side_base):
            raise ValueError("Сумма 2х сторон д.б. больше чем 3 сторона")
        self.__side_base = side_base
        self.__side_a = side_a
        self.__side_b = side_b
        self._area = round(self.__side_base * self.height * 0.5, 2)
        self._perimeter = round(self.__side_a + self.__side_b + self.__side_base, 2)
        self._name = 'Triangle'

    # Вычисление полупериметра -->> высоты
    @property
    def semi_perimeter(self):
        semi_perimeter = (self.__side_a + self.__side_b + self.__side_base) / 2
        return semi_perimeter

    # Вычисление высоты -->> площади
    @property
    def height(self):
        height = round((2 * (sqrt(self.semi_perimeter *
                                  (self.semi_perimeter - self.__side_base) *
                                  (self.semi_perimeter - self.__side_a) *
                                  (self.semi_perimeter - self.__side_b)))) / self.__sie_base, 2)
        return height
