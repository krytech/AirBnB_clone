#!/usr/bin/python3
"""Unittest for amenity."""
import os
import pep8
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for amenity."""

    @classmethod
    def setUpClass(self):
        """Set up test amenity."""
        self.amenity = Amenity()
        self.amenity.name = "Lots and lots of hula hoops"

    @classmethod
    def del_amenity(self):
        """Delete amenity after test."""
        del self.amenity

    def teardown(self):
        """Teardown."""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_amenity(self):
        """Test PEP8."""
        style = pep8.StyleGuide(quiet=True)
        errors = style.check_files(['models/amenity.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_instance(self):
        """Test instantiation."""
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes_amenity(self):
        """Test attributes."""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_subclass_amenity(self):
        """Test if amenity is a subclass of BaseModel."""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attri_types_amenity(self):
        """Test attribute types."""
        self.assertEqual(type(self.amenity.name), str)

    def test_save_amenity(self):
        """Test save()."""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_dict_amenity(self):
        """Test to_dict()."""
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
