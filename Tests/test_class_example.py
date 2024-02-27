#!/usr/bin/python3

import unittest
from class_example import Rectangle

class TestRectangle(unittest.TestCase):
    def test_area(self):
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.area(), 20)

if __name__ == '__main__':
    unittest.main()
