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


if __name__ == "__main__":
    unittest.main()