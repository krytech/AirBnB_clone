#!/usr/bin/python3
"""Unittest for place."""
import os
import pep8
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for Place."""

    @classmethod
    def setUpClass(self):
        """Set up test place."""
        self.place = Place()
        self.place.city_id = "123ab"
        self.place.user_id = "456cd"
        self.place.name = "Sanktem"
        self.place.description = "free ice cream"
        self.place.number_rooms = 500
        self.place.number_bathrooms = 5
        self.place.max_guest = 800000
        self.place.price_by_night = 200
        self.place.latitude = 150.0
        self.place.longitude = 20.0
        self.place.amenity_ids = ["12345-abjklmo"]

    @classmethod
    def del_place(self):
        """Delete place after test."""
        del self.place

    def teardown(self):
        """Teardown."""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_place(self):
        """Test PEP8."""
        style = pep8.StyleGuide(quiet=True)
        errors = style.check_files(['models/place.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_instance(self):
        """Test instantiation."""
        self.assertIsInstance(self.place, Place)

    def test_attributes_place(self):
        """Test attributes."""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)

    def test_subclass_place(self):
        """Test if place is a subclass of BaseModel."""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_attri_types_place(self):
        """Test attribute types."""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_save_place(self):
        """Test save()."""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_dict_place(self):
        """Test to_dict()."""
        self.assertEqual('to_dict' in dir(self.place), True)


if __name__ == "__main__":
    unittest.main()
