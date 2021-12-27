##########
# Author: Skylar Baker
# Title: Tests for text based call flow maker
##########

from CallFlowMaker import *
import unittest
from unittest.mock import patch, Mock

# This is just to populate the tests file so VSCode extensions pick the tests up properly
# Note to self: start all test functions with 'test' so extensions work properly
#class BlankTest(unittest.TestCase):
#    def test_nothing(self):
#        pass  

class TestHelpers(unittest.TestCase):
    @patch('builtins.input', side_effect=["a", "y", "", "Y"])
    def test_yes_input(self, inputs):
        self.assertTrue(get_yes_no_input("test q")) # Inputs: a, y
        self.assertTrue(get_yes_no_input("test q", 1)) # Inputs: (blank/enter)
        self.assertTrue(get_yes_no_input("test q", 0)) # Inputs: Y

    @patch('builtins.input', side_effect=["a", "n", "N", ""])
    def test_no_input(self, inputs):
        self.assertFalse(get_yes_no_input("test q")) # Inputs: a, n
        self.assertFalse(get_yes_no_input("test q", 1)) # Inputs: N
        self.assertFalse(get_yes_no_input("test q", 0)) # Inputs: (blank/enter)

    @patch('builtins.input', side_effect=["1", "1234", "456"])
    def test_ext_input(self, inputs):
        self.assertEqual(get_valid_extension("test q"), "1234") # Inputs: 1, 1234
        self.assertEqual(get_valid_extension("test q", 3), "456") # Inputs: 456

    @patch('builtins.input', side_effect=["", "12345678901", "1234", "1234567890", "1234567890", "(123)4567890", "(123) 4567890", "(123) 456-7890", "123 456 7890", "123-456-7890", "(123) 456 7890"])
    def test_valid_number(self, inputs):
        self.assertEqual(get_valid_phone_number("test q"), "1234567890") # Inputs: (blank/enter), 12345678901, 1234, 1234567890
        self.assertEqual(get_valid_phone_number("test q"), "1234567890") # Inputs: 1234567890
        self.assertEqual(get_valid_phone_number("test q"), "1234567890") # Inputs: (123)4567890
        self.assertEqual(get_valid_phone_number("test q"), "1234567890") # Inputs: (123) 4567890
        self.assertEqual(get_valid_phone_number("test q"), "1234567890") # Inputs: (123) 456-7890
        self.assertEqual(get_valid_phone_number("test q"), "1234567890") # Inputs: 123 456 7890
        self.assertEqual(get_valid_phone_number("test q"), "1234567890") # Inputs: 123-456-7890
        self.assertEqual(get_valid_phone_number("test q"), "1234567890") # Inputs: (123) 456 7890

    @patch('builtins.input', side_effect=["", "123", "12345678901", "1234", "1234", "123", "12345678901", "1234567890"])
    def test_get_valid_forward(self, inputs):
        self.assertEqual(get_valid_forward("test q"), "1234") # Inputs: (blank/enter), 123, 12345678901, 1234
        self.assertEqual(get_valid_forward("test q", 3), "123") # Inputs: 1234, 123
        self.assertEqual(get_valid_forward("test q"), "1234567890") # Inputs: 12345678901, 1234567890
        
    @patch('builtins.input', side_effect=["0", "1", "2", "3", "4", "5"])
    def test_get_line_type(self, inputs):
        self.assertEqual(get_line_type("1234"), LineType.TOD) # Inputs: 0, 1
        self.assertEqual(get_line_type("1234"), LineType.MLHG) # Inputs: 2
        self.assertEqual(get_line_type("1234"), LineType.AA) # Inputs: 3
        self.assertEqual(get_line_type("1234"), LineType.SUB) # Inputs: 4
        self.assertEqual(get_line_type("1234"), LineType.VM) # Inputs: 5

    @patch('builtins.input', side_effect=["11", "5", "4", "5", "5", "5"])
    def test_get_num_in_range(self, inputs):
        self.assertEqual(get_num_in_range("test"), 5) # Inputs: 11, 5
        self.assertEqual(get_num_in_range("test", num_min=5), 5) # Inputs: 4, 5
        self.assertEqual(get_num_in_range("test", num_max=6), 5) # Inputs: 5
        self.assertEqual(get_num_in_range("test", num_min=5, num_max=5), 5) # Inputs: 5

class TestLines(unittest.TestCase):
    @patch('builtins.input', side_effect=["testing", "5", "1234567890", "12340", "Main TOD", "1"])
    def test_setup(self, inputs):
        bg = {
            "name": "testing",
            "ext_len": "5",
            "main_num": "1234567890",
            "main_ext": "12340",
            "main_type": LineType.TOD
        }
        output = setup()
        self.assertEqual(bg, output)

    @patch('builtins.input', side_effect=["2", "8-5", "12345", "All other times", "1234567890"])
    def test_make_tod(self, inputs):
        line = {
            "ext": "12340",
            "name": "Main TOD",
            "line_type": LineType.TOD
        }
        tod = {
            "ext": "12340",
            "name": "Main TOD",
            "line_type": LineType.TOD,
            "schedules": [
                {
                    "active": "8-5",
                    "forward": "12345"
                }, {
                    "active": "All other times",
                    "forward": "1234567890"
                }
            ],
            "connections": [
                {"to_ext": "12345", "from_ext": "12340", "label": "8-5"},
                {"to_ext": "1234567890", "from_ext": "12340", "label": "All other times"}
            ]
        }
        test = make_tod(line)
        self.assertEqual(test, tod)


if __name__ == "__main__":
    unittest.main()