Домашнее задание

ООП и Pytest на практике
Цель:

Научиться писать код в ООП стиле и покрывать его тестами.
Описание/Пошаговая инструкция выполнения домашнего задания:

Создать базовый класс геометрической фигуры (Figure).
Реализовать классы геометрических фигур Треугольник, Прямоугольник, Квадрат, Круг (Triangle, Rectangle, Square, Circle).

    Каждый класс должен располагаться в отдельном файле с соответствующим названием (например class Triangle => Triangle.py).
    Все файлы с классами должны находиться в папке src/ в корне репозитория.
    Треугольник должен задаваться тремя сторонами, если треугольник создать нельзя то класс должен вернуть None 1 Часть. Каждая фигура должна иметь атрибуты: name - название фигуры, area (вычисляемое!) - площадь, perimeter (вычисляемое!) - периметр (сумма длин сторон или длину окружности) Все вычисляемые свойства должны вычисляться по формулам для соответствующих геометрических фигур (никакого хардкода значений). Каждая фигура должна реализовать метод add_area(figure) который должен принимать другую геометрическую фигуру и возвращать сумму площадей этих фигур. Если передана не геометрическая фигура, то нужно выбрасывать ошибку (raise ValueError) и сообщать что передан неправильный класс. Пример работы с одним из классов фигуры:

                square = Square(10) # Так создаем квадрат со стороной 10
                square.area
                100
                triangle = Triangle(13, 14, 15) # Так создаем треугольник со сторонами 13, 14, 15
                triangle.area
                84
                triangle.add_area(square)
                184

    Часть. Написать тесты с использованием pytest на эти классы. Глубину покрытия и объем определить самостоятельно, но минимум проверить реализацию всех указанных требований для каждого класса.

    Все тесты должны располагаться в папке tests/ в корне репозитория.

Критерии оценки:

    Будет оцениваться глубина использования парадигмы ООП.
    Встроенные декораторы, наследование, отсутствие дублирования кода.
    Если какой-то метод выполняет одно и тоже во всех классах наследниках, то он должен принадлежать родительскому классу.
    Задание сдавать в формате pull-request.
    Соблюдение минимального кодстайла.
    Никаих print'ов, закомментированного кода и лишних файлов быть не должно.

