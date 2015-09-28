# python imports
import unittest
from random import random, randint
# local imports
from .main import fibo


class TestFib(unittest.TestCase):
    '''
    Test suite for `fibo` function.
    '''
    def test_negative_input(self):
        for i in range(100):
            self.assertRaises(
                ValueError,
                lambda: fibo(randint(-100, -1))
            )

    def test_decimal_input(self):
        for i in range(100):
            decimal = 100 * random()
            if decimal != 0:
                self.assertRaises(
                    ValueError,
                    lambda: fibo(decimal)
                )

    def test_sample_input(self):
        self.assertEqual(fibo(6), 8)
