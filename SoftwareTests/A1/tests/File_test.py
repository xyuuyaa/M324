import unittest
from src.File import *
import os

class TestFile(unittest.TestCase):
    test_file = "test_file.txt"

    def test_create_file(self):
        File.create_file(self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

    def test_write_to_file(self):
        File.create_file(self.test_file)
        File.write_to_file(self.test_file, "test")
        with open(self.test_file, 'r') as f:
            content = f.read()
        self.assertEqual(content, "test")

    def test_read_from_file(self):
        # test first case: file does not exist
        result = File.read_from_file(self.test_file)
        self.assertEqual(result, f"Error: '{self.test_file}' does not exist.")
        
        # test second case: file exists
        File.create_file(self.test_file)
        result = File.read_from_file(self.TEST_FILE)
        self.assertEqual(result, '')
