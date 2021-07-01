#!/usr/bin/python3
"""Unittest for city."""
import os
import pep8
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for city."""

    @classmethod
    def setUpClass(self):
        """Set up test city."""
        self.city = City()
        self.city.state_id = "NY"
        self.city.name = "NYC"

    @classmethod
    def del_city(self):
        """Delete city after test."""
        del self.city

    def teardown(self):
        """Teardown."""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_city(self):
        """Test PEP8."""
        style = pep8.StyleGuide(quiet=True)
        errors = style.check_files(['models/city.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_instance(self):
        """Test instantiation."""
        self.assertIsInstance(self.city, City)

    def test_attributes_city(self):
        """Test attributes."""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_subclass_city(self):
        """Test if city is a subclass of BaseModel."""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attri_types_city(self):
        """Test attribute types."""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_save_city(self):
        """Test save()."""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_dict_city(self):
        """Test to_dict()."""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
