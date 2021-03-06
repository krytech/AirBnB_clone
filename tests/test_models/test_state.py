#!/usr/bin/python3
"""Unittest for state."""
import unittest
import pep8
import os
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State."""

    @classmethod
    def setUpClass(self):
        """Set up test state."""
        self.state = State()
        self.state.name = "NY"

    @classmethod
    def del_state(self):
        """Delete state after test."""
        del self.state

    def teardown(self):
        """Teardown."""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_state(self):
        """Test PEP8."""
        style = pep8.StyleGuide(quiet=True)
        errors = style.check_files(['models/state.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_instance(self):
        """Test instantiation."""
        self.assertIsInstance(self.state, State)

    def test_attributes_state(self):
        """Test attributes."""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_subclass_state(self):
        """Test if State is a subclass of BaseModel."""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attri_types_state(self):
        """Test attribute types."""
        self.assertEqual(type(self.state.name), str)

    def test_save_state(self):
        """Test save()."""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_dict_state(self):
        """Test to_dict()."""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
