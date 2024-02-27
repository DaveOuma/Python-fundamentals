#!/usr/bin/python3

import unittest
import os
from file_io_example import write_to_file, read_from_file

class TestFileIO(unittest.TestCase):
    def setUp(self):
        self.filename = "test_file.txt"

    def test_write_and_read_file(self):
        content = "Hello, world!"
        write_to_file(self.filename, content)
        self.assertEqual(read_from_file(self.filename), content)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

if __name__ == '__main__':
    unittest.main()
