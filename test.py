import unittest
from polynom import Polynom
from polynom import Poly


class TestPolynom(unittest.TestCase):

    def setUp(self):
        self.polynom = Poly("x^3+x^2+x+5")
        self.otherpolynom = Poly("x^2-2x-5")

    def test_add(self):
        result = self.polynom.__add__(self.otherpolynom).__str__()
        self.assertEqual(result, "x^3+2x^2+6x")

    def test_sub(self):
        result = self.polynom.__sub__(self.otherpolynom).__str__()
        self.assertEqual(result, "x^3+3x+3")

    def test_mul(self):
        result = self.polynom.__mul__(self.otherpolynom).__str__()
        self.assertEqual(result, "x^5+6x^4+x^3+5x^2+6x+3")

    def test_floordiv(self):
        result = self.polynom.__floordiv__(self.otherpolynom).__str__()
        self.assertEqual(result, "x+3")

    def test_mod(self):
        result = self.polynom.__mod__(self.otherpolynom).__str__()
        self.assertEqual(result, "5x+6")


if __name__ == "__main__":
    unittest.main()