#!/usr/bin/python3
"""Unittest BaseModel"""
import unittest
import pep8
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test BaseModel"""

    @classmethod
    def setUpClass(self):
        """Set up test basemodel"""
        self.basemodel = BaseModel()
        self.basemodel.name = "Buffy"

    @classmethod
    def del_basemodel(self):
        """Deletes basemodel after test"""
        del self.basemodel

    def teardown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_basemodel(self):
        """Pep8 test for basemodel"""
        style = pep8.StyleGuide(quiet=True)
        errors = style.check_files(['models/base_model.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_instance(self):
        """Test to check if the basemodel is instantiated"""
        self.assertIsInstance(self.basemodel, BaseModel)
        self.assertTrue(hasattr(self.basemodel, "id"))
        self.assertTrue(hasattr(self.basemodel, "created_at"))
        self.assertTrue(hasattr(self.basemodel, "updated_at"))

    def test_save_basemodel(self):
        """Test if the save works"""
        self.basemodel.save()
        self.assertNotEqual(
            self.basemodel.created_at, self.basemodel.updated_at
        )

    def test_dict_basemodel(self):
        """Test if dictionary works"""
        self.assertTrue('to_dict' in dir(self.basemodel))
        d = self.basemodel.to_dict()
        self.assertIsInstance(d, dict)
        self.assertTrue("__class__" in d)
        self.assertTrue("id" in d)
        self.assertTrue("created_at" in d)
        self.assertTrue("updated_at" in d)

    def test_method_basemodel(self):
        """Test if Basemodel have methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))


if __name__ == '__main__':
    unittest.main()
