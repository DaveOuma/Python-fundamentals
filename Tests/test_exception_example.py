#!/usr/bin/python3

import unittest
from exception_example import divide

class TestExceptionExample(unittest.TestCase):
    def test_divide_by_zero(self):
        self.assertIsNone(divide(10, 0))

    def test_divide_numbers(self):
        self.assertEqual(divide(10,2), 5)

if __name__== '__main__':
    unittest.main()
