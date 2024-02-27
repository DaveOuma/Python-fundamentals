#!/usr/bin/python3

import unittest
from import_example import square_root

class TestImportExample(unittest.TestCase):
    def test_square_root(self):
        self.assertEqual(square_root(9), 3)

if __name__ == '__main__':
    unittest.main()
