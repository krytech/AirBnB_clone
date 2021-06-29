#!/usr/bin/python3
"""Unittest for state"""
import unittest
import pep8
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State"""

    def test_pep8_state(self):
        """Pep8 test for state"""
        style = pep8.StyleGuide(quiet=True)
        errors = style.check_files(['models/state.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    @classmethod
    def setUpClass(self):
        """Set up test state"""
        self.state = State()
        self.state.name = "NY"

if __name__ == "__main__":
    unittest.main()
