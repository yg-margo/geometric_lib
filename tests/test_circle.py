import math
import unittest
import sys
import os

# Добавляем родительскую директорию в путь для импорта модулей
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import circle


class CircleTestCase(unittest.TestCase):

    def test_area_positive_radius(self):
        """
        Тестирует вычисление площади круга с положительным радиусом.

        Проверяет корректность работы функции area() с обычными положительными значениями.
        Использует assertAlmostEqual для сравнения чисел с плавающей точкой.

        Тестируемая функция:
            circle.area(r) - вычисляет площадь круга

        Входные данные:
            r = 5

        Ожидаемый результат:
            π * 5² ≈ 78.53975

        Пример выполнения:
            >>> circle.area(5)
            78.53981633974483
        """
        result = circle.area(5)
        expected = math.pi * 25
        self.assertAlmostEqual(result, expected, places=4)

    def test_area_zero_radius(self):
        """
        Тестирует вычисление площади круга с нулевым радиусом.

        Проверяет обработку граничного случая, когда радиус равен нулю.
        Площадь должна равняться нулю.

        Тестируемая функция:
            circle.area(r) - вычисляет площадь круга

        Входные данные:
            r = 0

        Ожидаемый результат:
            0

        Пример выполнения:
            >>> circle.area(0)
            0
        """
        result = circle.area(0)
        self.assertEqual(result, 0)

    def test_area_unit_radius(self):
        """
        Тестирует вычисление площади круга с единичным радиусом.

        Проверяет работу функции с радиусом равным 1.
        Результат должен быть равен числу π.

        Тестируемая функция:
            circle.area(r) - вычисляет площадь круга

        Входные данные:
            r = 1

        Ожидаемый результат:
            π ≈ 3.14159

        Пример выполнения:
            >>> circle.area(1)
            3.141592653589793
        """
        result = circle.area(1)
        expected = math.pi
        self.assertAlmostEqual(result, expected, places=3)

    def test_perimeter_positive_radius(self):
        """
        Тестирует вычисление периметра круга с положительным радиусом.

        Проверяет корректность работы функции perimeter() с положительными значениями.
        Использует assertAlmostEqual для сравнения чисел с плавающей точкой.

        Тестируемая функция:
            circle.perimeter(r) - вычисляет периметр (длину окружности)

        Входные данные:
            r = 5

        Ожидаемый результат:
            2 * π * 5 ≈ 31.4159

        Пример выполнения:
            >>> circle.perimeter(5)
            31.41592653589793
        """
        result = circle.perimeter(5)
        expected = 2 * 3.14159 * 5
        self.assertAlmostEqual(result, expected, places=4)

    def test_perimeter_zero_radius(self):
        """
        Тестирует вычисление периметра круга с нулевым радиусом.

        Проверяет обработку граничного случая, когда радиус равен нулю.
        Периметр должен равняться нулю.

        Тестируемая функция:
            circle.perimeter(r) - вычисляет периметр круга

        Входные данные:
            r = 0

        Ожидаемый результат:
            0

        Пример выполнения:
            >>> circle.perimeter(0)
            0
        """
        result = circle.perimeter(0)
        self.assertEqual(result, 0)

    def test_perimeter_unit_radius(self):
        """
        Тестирует вычисление периметра круга с единичным радиусом.

        Проверяет работу функции с радиусом равным 1.
        Результат должен быть равен 2π.

        Тестируемая функция:
            circle.perimeter(r) - вычисляет периметр круга

        Входные данные:
            r = 1

        Ожидаемый результат:
            2π ≈ 6.28318

        Пример выполнения:
            >>> circle.perimeter(1)
            6.283185307179586
        """
        result = circle.perimeter(1)
        expected = 2 * 3.14159
        self.assertAlmostEqual(result, expected, places=4)


if __name__ == '__main__':
    unittest.main()