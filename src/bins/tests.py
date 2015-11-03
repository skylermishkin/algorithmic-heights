# python imports
import unittest
from random import random, randint
# local imports
from .util import binarySearch


class TestBinarySearch(unittest.TestCase):
    '''
    Test suite for `binarySearch` function.
    '''
    def test_small_array(self):
        self.assertEqual(binarySearch([1, 2, 3], 2), 1)
