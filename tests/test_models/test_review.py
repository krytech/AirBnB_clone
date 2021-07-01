#!/usr/bin/python3
"""Unittest for review."""
import os
import pep8
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for review."""

    @classmethod
    def setUpClass(self):
        """Set up test review."""
        self.review = Review()
        self.review.place_id = "1234-znywt"
        self.review.user_id = "1234-sdgoik"
        self.review.text = "Amaaaaaaazing!!!"

    @classmethod
    def del_review(self):
        """Delete review after test."""
        del self.review

    def teardown(self):
        """Teardown."""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_review(self):
        """Test PEP8."""
        style = pep8.StyleGuide(quiet=True)
        errors = style.check_files(['models/review.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_instance(self):
        """Test instantiation."""
        self.assertIsInstance(self.review, Review)

    def test_attributes_review(self):
        """Test attributes."""
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)
        self.assertTrue('text' in self.review.__dict__)

    def test_subclass_review(self):
        """Test if review is a subclass of BaseModel."""
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_attri_types_review(self):
        """Test attribute types."""
        self.assertEqual(type(self.review.text), str)
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)

    def test_save_review(self):
        """Test save()."""
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_dict_review(self):
        """Test to_dict()"""
        self.assertEqual('to_dict' in dir(self.review), True)


if __name__ == "__main__":
    unittest.main()
