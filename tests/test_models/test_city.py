#!/usr/bin/python3
"""Unittest for city"""
import unittest
import pep8
import os
from models.base_model import BaseModel
from models.city import City


class Testcity(unittest.TestCase):
    """Test cases for city"""

    @classmethod
    def setUpClass(self):
        """Set up test city"""
        self.city = City()
        self.city.state_id = "NY"
        self.city.name = "NYC"

    @classmethod
    def del_city(self):
        """Deletes city after test"""
        del self.city

    def teardown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_city(self):
        """Pep8 test for city"""
        style = pep8.StyleGuide(quiet=True)
        errors = style.check_files(['models/city.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_instance(self):
        """Test to check if the city is instantiated"""
        self.assertIsInstance(self.city, City)

    def test_attributes_city(self):
        """Test to check if city has all attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_subclass_city(self):
        """Test to check if city is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attri_types_city(self):
        """Test for attribute types for city"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_save_city(self):
        """Test if the save works"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_dict_city(self):
        """Test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
