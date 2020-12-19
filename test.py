import unittest
from polynom import Polynom
from polynom import Poly


class TestPolynom(unittest.TestCase):

    def setUp(self):
        # self.polynom = Poly("x^3+x^2+x+5")
        # self.otherpolynom = Poly("x^2-2x-5")
        # self.polynom = Poly("112x^4+58x^3-31x^2+107x-66")
        # self.polynom = Poly("x^4+1")
        # self.polynom = Poly("x^2+2x+1")
        # self.polynom = Poly("x^4+7x^3+8x^2+7x+1")
        # self.polynom = Poly("x^2+5x+6")
        # self.polynom = Poly("x^3+6x^2+11x+6")
        self.polynom = Poly("8x^6+9x^5+2x^4+12x^3+x+12")
        # self.polynom = Poly("8x^7+4x^6+11x^5+x^4+12x^3+x^2+12")
        # self.polynom = Poly("x^4+6x^3+12x+4")
        # self.polynom = Poly("9x^2+x+5")

        # self.polynom = Poly("112x^4+58x^3-31x^2+107x-66")
        # self.otherpolynom = Poly("x^2+2x+1")

        # self.polynom = Poly("8x^6+9x^5+2x^4+12x^3+x+12")
        # self.otherpolynom = Poly("x+1")

        # self.polynom = Poly("11x^4+5x^3+11x^2+9x+10")

        # первая строка матрицы Q = (1, 0, 0, 0), deg = 4
        # изначальный полином x^4+4x^3+x^2+2x+8
        # self.polynom = Poly("x^4+4x^3+x^2+2x+8")

        # вторая строка матрицы Q - остаток от деления:
        # self.polynom = Poly("x^13")
        # self.otherpolynom = Poly("x^4+4x^3+x^2+2x+8")

        # возведем результат в квадрат
        # self.polynom = Poly("5x^3+4x^2+12")
        # self.otherpolynom = Poly("5x^3+4x^2+12")

        # третья строка матрицы Q - остаток от деления:
        # self.polynom = Poly("12x^6+x^5+3x^4+3x^3+5x^2+1")
        # self.otherpolynom = Poly("x^4+4x^3+x^2+2x+8")

        # домножим x^2k на x^k
        # self.polynom = Poly("5x^3+4x^2+12")
        # self.otherpolynom = Poly("12x^6+x^5+3x^4+3x^3+5x^2+1")

        # четвертая строка матрицы Q - остаток от деления:
        # self.polynom = Poly("8x^9+x^8+6x^7+2x^6+10x^5+4x^4+2x^3+12x^2+12")
        # self.otherpolynom = Poly("x^4+4x^3+x^2+2x+8")

        # for berlikamp:
        # self.polynom = Poly("x^2-4x+2")  # x^4+3x-2

    def test_add(self):
        result = self.polynom.__add__(self.otherpolynom).__str__()
        self.assertEqual(result, "x^3+2x^2+6x")

    def test_sub(self):
        result = self.polynom.__sub__(self.otherpolynom).__str__()
        self.assertEqual(result, "x^3+3x+3")

    def test_mul(self):
        result = self.polynom.__mul__(self.otherpolynom).__str__()
        # print("Multiplication result is ", result)
        self.assertEqual(result, "x^5+6x^4+x^3+5x^2+6x+3")

    def test_floordiv(self):
        result = self.polynom.__floordiv__(self.otherpolynom).__str__()
        # print('\nResult of division is', result)
        self.assertEqual(result, "x+3")

    def test_mod(self):
        result = self.polynom.__mod__(self.otherpolynom).__str__()
        print("Remainder of the division is ", result)
        self.assertEqual(result, "5x+6")

    def test_berlekamp(self):
        result = self.polynom.berlekamp_first().__str__()
        print("The resut is ", result)
        # self.assertEqual(result, "(x-2)(x-2)")  # "(x^2+6x+2)(x^2+x+6)"
        # self.assertEqual(result, "(x^2+9x+9)(8x^2+12x+10)")
        self.assertEqual(result, "(x^2+9x+9)(x^2+8x+11)")


if __name__ == "__main__":
    unittest.main()
