import unittest
from unittest import TestCase

from calc import Calc


class TestSum(TestCase):
    """
    testing func sum in the calc
    """

    def test_001(self):
        self.assertEqual(Calc.sum(3, 7), 10)
        self.assertEqual(Calc.sum(-3, -7), -10)
        self.assertEqual(Calc.sum(3, -7), -4)

    def test_002(self):
        self.assertIsInstance(Calc.sum(4, -2), int)
        self.assertIsInstance(Calc.sum(4.0, -1), float)
        self.assertIsInstance(Calc.sum(3, 0.5), float)

    def test_003(self):
        with self.assertRaises(TypeError):
            Calc.sum("0", 0)


if __name__ == '__main__':
    unittest.main()
