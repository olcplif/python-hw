import unittest
from unittest import TestCase

from calc import Calc


class TestDiv(TestCase):
    """
    testing func div in the calc
    """

    def test_001(self):
        self.assertEqual(Calc.div(8, -2), -4.0)
        self.assertEqual(Calc.div(-9, -3), 3.0)
        self.assertEqual(Calc.div(4, 2.0), 2.0)
        self.assertEqual(Calc.div(0, 2.0), 0.0)

    def test_002(self):
        self.assertIsInstance(Calc.div(4, -2), float)
        self.assertIsInstance(Calc.div(4.0, -1), float)
        self.assertIsInstance(Calc.div(3, 0.5), float)

    def test_003(self):
        with self.assertRaises(TypeError):
            Calc.div("0", 0)
        with self.assertRaises(ZeroDivisionError):
            Calc.div(9, 0)


if __name__ == '__main__':
    unittest.main()
