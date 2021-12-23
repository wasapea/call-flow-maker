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
        self.assertTrue(get_yes_no_input("test q"))
        self.assertTrue(get_yes_no_input("test q", 1))
        self.assertTrue(get_yes_no_input("test q", 0))

    @patch('builtins.input', side_effect=["a", "n", "N", ""])
    def test_no_input(self, inputs):
        self.assertFalse(get_yes_no_input("test q"))
        self.assertFalse(get_yes_no_input("test q", 1))
        self.assertFalse(get_yes_no_input("test q", 0))


if __name__ == "__main__":
    unittest.main()