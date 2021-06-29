#!/usr/bin/python3
"""Unittest for amenity"""
import unittest
import pep8
import os
from models.base_model import BaseModel
from models.amenity import Amenity


class Testamenity(unittest.TestCase):
    """Test cases for amenity"""

    @classmethod
    def setUpClass(self):
        """Set up test amenity"""
        self.amenity = Amenity()
        self.amenity.name = "Lots and lots of hula hoops"

    @classmethod
    def del_amenity(self):
        """Deletes amenity after test"""
        del self.amenity

    def teardown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_amenity(self):
        """Pep8 test for amenity"""
        style = pep8.StyleGuide(quiet=True)
        errors = style.check_files(['models/amenity.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_instance(self):
        """Test to check if the amenity is instantiated"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes_amenity(self):
        """Test to check if amenity has all attributes"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_subclass_amenity(self):
        """Test to check if amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attri_types_amenity(self):
        """Test for attribute types for amenity"""
        self.assertEqual(type(self.amenity.name), str)

    def test_save_amenity(self):
        """Test if the save works"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_dict_amenity(self):
        """Test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
