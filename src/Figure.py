class Figure:
    _name = None
    _area = None
    _perimeter = None

    # Добавление площади
    def add_area(self, other_figure):
        if isinstance(other_figure, Figure):
            sum_areas = self._area + other_figure._area
            return sum_areas
        else:
            raise ValueError("Ошибка класса")

    # Получение периметра
    def get_perimeter(self):
        return self._perimeter


# Получение площади
def get_area(self):
    return self._area

    # Получение имени
    def get_name(self):
        return self._name
