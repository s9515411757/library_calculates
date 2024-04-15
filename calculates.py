import math


def circle_area(radius: [float, int]) -> float:
    """
    Функция для вычисления площади круга.

    :param radius: (float | int): Радиус круга.
    :return: (float): Площадь круга.
    """
    return math.pi * radius**2


def triangle_area(a: [float, int], b: [float, int], c: [float, int]) -> float:
    """
    Функция для вычисления площади треугольника.

    :param a: (float | int): Длина первой стороны треугольника.
    :param b: (float | int): Длина второй стороны треугольника.
    :param c: (float | int): Длина третьей стороны треугольника.
    :return: (float): Площадь треугольника
    """
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def is_right_triangle(
        a: [float, int],
        b: [float, int],
        c: [float, int]
        ) -> bool:
    """
    Функция для определения, является ли треугольник прямоугольным.

    :param a: (float | int): Длина первой стороны треугольника.
    :param b: (float | int): Длина второй стороны треугольника.
    :param c: (float | int): Длина третьей стороны треугольника.
    :return: (bool): Треугольник прямоугольный или нет.
    """
    sides = [a, b, c]
    max_side = max(sides)
    sides.remove(max_side)
    return max_side**2 == sides[0]**2 + sides[1]**2
