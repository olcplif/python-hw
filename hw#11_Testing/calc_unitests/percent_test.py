import unittest
from unittest import TestCase

from calc import Calc


class TestPercent(TestCase):
    """
    testing func percent in the calc
    """

    def test_001(self):
        self.assertEqual(Calc.percent(10, 10), 1)
        self.assertEqual(Calc.percent(-100, 50), -50)

    def test_002(self):
        self.assertIsInstance(Calc.percent(4, 2), float)
        self.assertIsInstance(Calc.percent(4.0, 1), float)
        self.assertIsInstance(Calc.percent(3, 0.5), float)

    def test_003(self):
        with self.assertRaises(TypeError):
            Calc.percent("0", 10)
        with self.assertRaises(ZeroDivisionError):
            Calc.div(36, 0)


if __name__ == '__main__':
    unittest.main()
