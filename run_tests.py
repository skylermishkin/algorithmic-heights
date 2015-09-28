#!/usr/local/bin/python3

'''
Runs the entire test suite.
'''

# import all `TestCase`s
from src.fibo.tests import *

# if this is being run as a script
if __name__ == '__main__':
    import unittest
    # run the tests
    unittest.main()
