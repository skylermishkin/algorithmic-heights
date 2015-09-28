import unittest
from main import fib

class TestFib(unittest.TestCase):

    def test_fib_with_negative_input(self):
        self.assertRaises(ValueError, lambda: fib(-1))

    def test_fib_with_sample_input(self):
        self.assertEqual(fib(6), 8)

if __name__ == '__main__':
    unittest.main()
