import unittest
from unittest import TestCase

from calc import Calc


class TestMinus(TestCase):
    """
    testing func minus in the calc
    """

    def test_001(self):
        self.assertEqual(Calc.minus(8, 2), 6)
        self.assertEqual(Calc.minus(-9, -3), -6)
        self.assertEqual(Calc.minus(4, 2.0), 2.0)

    def test_002(self):
        self.assertIsInstance(Calc.minus(4, -2), int)
        self.assertIsInstance(Calc.minus(4.0, -1), float)
        self.assertIsInstance(Calc.minus(3, 0.5), float)

    def test_003(self):
        with self.assertRaises(TypeError):
            Calc.minus("0", 0)


if __name__ == '__main__':
    unittest.main()
