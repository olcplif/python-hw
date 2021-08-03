import unittest
from unittest import TestCase

from calc import Calc


class TestRoot(TestCase):
    """
    testing func root in the calc
    """

    def test_001(self):
        self.assertEqual(Calc.root(9), 3)
        self.assertEqual(Calc.root(9.0), 3.0)
        self.assertEqual(Calc.root(8, 3), 2.0)

    def test_002(self):
        self.assertIsInstance(Calc.root(4), float)
        self.assertIsInstance(Calc.root(4.0), float)

    def test_003(self):
        with self.assertRaises(TypeError):
            Calc.root("0")


if __name__ == '__main__':
    unittest.main()
