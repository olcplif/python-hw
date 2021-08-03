import unittest
from unittest import TestCase

from calc import Calc


class TestMul(TestCase):
    """
    testing func mul in the calc
    """

    def test_001(self):
        self.assertEqual(Calc.mul(0, 0), 0)
        self.assertEqual(Calc.mul(-1, -1), 1)
        self.assertEqual(Calc.mul(4, 2.0), 8.0)

    def test_002(self):
        self.assertIsInstance(Calc.mul(4, -2), int)
        self.assertIsInstance(Calc.mul(4.0, -1), float)
        self.assertIsInstance(Calc.mul(3, 0.5), float)

    def test_003(self):
        with self.assertRaises(TypeError):
            Calc.mul("0", "0")


if __name__ == '__main__':
    unittest.main()
