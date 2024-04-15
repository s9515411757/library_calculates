import math
import unittest

from calculates import circle_area, triangle_area, is_right_triangle


class TestGeometryFunctions(unittest.TestCase):
    def test_circle_area(self):
        # Проверка для радиуса 1
        self.assertAlmostEqual(circle_area(1), math.pi)
        # Проверка для радиуса 0
        self.assertAlmostEqual(circle_area(0), 0)

    def test_triangle_area(self):
        # Проверка для треугольника со сторонами 3, 4, 5
        self.assertAlmostEqual(triangle_area(3, 4, 5), 6)
        # Проверка для треугольника со сторонами 6, 8, 10
        self.assertAlmostEqual(triangle_area(6, 8, 10), 24)

    def test_is_right_triangle(self):
        # Проверка для прямоугольного треугольника
        self.assertTrue(is_right_triangle(3, 4, 5))
        # Проверка для непрямоугольного треугольника
        self.assertFalse(is_right_triangle(3, 3, 3))
        # Проверка для прямоугольного треугольника
        self.assertTrue(is_right_triangle(7, 24, 25))


if __name__ == '__main__':
    unittest.main()