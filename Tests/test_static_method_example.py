#!/usr/bin/python3

import unittest
from static_method_example import StringUtils

class TestStringUtils(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(StringUtils.is_palindrome("radar"))
        self.assertFalse(StringUtils.is_palindrome("hello"))

if __name__ == '__main__':
    unittest.main()
