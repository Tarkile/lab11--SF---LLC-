# https://github.com/Tarkile/lab11--SF---LLC-
# partner 1: Samuel Finlinson
# partner 2: Leonardo Lopez-Casula

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 4), 3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(-1, -4), 3)
        self.assertEqual(subtract(10, 20), -10)

    def test_multiply(self): # 3 assertions
         self.assertEqual(mul(3, 4), 12)
         self.assertEqual(mul(-2, 5), -10)
         self.assertEqual(mul(0, 100), 0)

    def test_divide(self): # 3 assertions
         self.assertEqual(div(10, 2), 5)
         self.assertEqual(div(-9, 3), -3)
         with self.assertRaises(ZeroDivisionError):
             div(5, 0)

    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(log(10, 100), 2.0)
        self.assertAlmostEqual(log(2, 8), 3.0)
        self.assertAlmostEqual(log(4, 16), 2.0)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-2, 8)

    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
           logarithm(0, 10)


    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(8, 15), 17.0)

    def test_sqrt(self):
         self.assertAlmostEqual(square_root(9), 3.0)
         self.assertAlmostEqual(square_root(0), 0.0)
         with self.assertRaises(ValueError):
             square_root(-4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
