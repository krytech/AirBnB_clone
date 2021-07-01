#!/usr/bin/python3
"""Unittest for user."""
import os
import pep8
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for user."""

    @classmethod
    def setUpClass(self):
        """Set up test user."""
        self.user = User()
        self.user.first_name = "Xena"
        self.user.last_name = "Warrior Princess"
        self.user.email = "XenaWarrior@princess.com"
        self.user.password = "Hiya"

    @classmethod
    def del_user(self):
        """Delete user after test."""
        del self.user

    def teardown(self):
        """Teardown."""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_user(self):
        """Test PEP8"""
        style = pep8.StyleGuide(quiet=True)
        errors = style.check_files(['models/user.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_instance(self):
        """Test instantiation."""
        self.assertIsInstance(self.user, User)

    def test_attributes_user(self):
        """Test attributes."""
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_subclass_user(self):
        """Test if user is a subclass of BaseModel."""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_attri_types_user(self):
        """Test attribute types."""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)

    def test_save_user(self):
        """Test save()."""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_dict_user(self):
        """Test to_dict()."""
        self.assertEqual('to_dict' in dir(self.user), True)


if __name__ == "__main__":
    unittest.main()
