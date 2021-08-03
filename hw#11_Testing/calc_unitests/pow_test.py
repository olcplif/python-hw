import unittest
from unittest import TestCase

from calc import Calc


class TestPow(TestCase):
    """
    testing func pow in the calc
    """

    def test_001(self):
        self.assertEqual(Calc.pow(10, 2), 100)
        self.assertEqual(Calc.pow(-10, 2), 100)
        self.assertEqual(Calc.pow(100000000, 0), 1)

    def test_002(self):
        self.assertIsInstance(Calc.pow(4, 2), int)
        self.assertIsInstance(Calc.pow(4.0, 1), float)
        self.assertIsInstance(Calc.pow(3, 0.5), float)

    def test_003(self):
        with self.assertRaises(TypeError):
            Calc.pow("0", 10)


if __name__ == '__main__':
    unittest.main()
