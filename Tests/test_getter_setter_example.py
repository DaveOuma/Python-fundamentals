#!/usr/bin/python3

import unittest
from getter_setter_example import Student

class TestStudent(unittest.TestCase):
    def test_getters_and_setters(self):
        student = Student("Alice", 20)
        self.assertEqual(student.get_name(), "Alice")
        self.assertEqual(student.get_age(), 20)
        student.set_name("Bob")
        student.set_age(22)
        self.assertEqual(student.get_name(), "Bob")
        self.assertEqual(student.get_age(), 22)

if __name__ == '__main__':
    unittest.main()
