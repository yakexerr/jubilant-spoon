import unittest

from hw23.lib.first import triangle_type


class MyTestCase(unittest.TestCase):
    def test_s1(self):
        self.assertEqual("Равнобедренный", triangle_type(3, 3, 4))

    def test_s2(self):
        self.assertEqual("Равносторонний", triangle_type(3, 3, 3))

    def test_s3(self):
        self.assertEqual("Разносторонний", triangle_type(3, 5, 4))

    def test_s4(self):
        self.assertEqual("Такого треугольника не существует", triangle_type(1, 1, 3))

    def test_s5(self):
        self.assertEqual("Стороны треугольника должны быть больше нуля", triangle_type(-1, -1, -1))


if __name__ == '__main__':
    unittest.main()
