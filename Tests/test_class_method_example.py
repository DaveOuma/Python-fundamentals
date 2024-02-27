#!/usr/bin/python3

import unittest
from class_method_example import MathOperations

class TestMathOperations(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(MathOperations.multiply(3, 4), 12)

if __name__ == '__main__':
    unittest.main()
