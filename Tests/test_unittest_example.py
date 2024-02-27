#!/usr/bin/python3

import unittest
from unittest_example import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-3, -5), -8)

if __name__ == '__main__':
    unittest.main()
