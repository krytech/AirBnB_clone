#!/usr/bin/python3
"""FileStorage unit test."""
import unittest
import os
import pep8
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test FileStorage class."""

    def test_instance(self):
        file_storage = FileStorage()
        self.assertIsInstance(file_storage, FileStorage)

    def test_class_fields(self):
        file_storage = FileStorage()
        self.assertTrue(hasattr(file_storage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(file_storage, "_FileStorage__objects"))

    def test_all(self):
        file_storage = FileStorage()
        all = file_storage.all()
        self.assertIsInstance(all, dict)
        self.assertEqual(all, {})
        self.assertEqual(all, file_storage._FileStorage__objects)

    def test_new(self):
        file_storage = FileStorage()
        obj = BaseModel()
        file_storage.new(obj)

        self.assertEqual(len(file_storage.all()), 1)
        self.assertTrue(obj in file_storage.all().values())

    def test_save(self):
        file_storage = FileStorage()
        test_path = "unittest_FileStorage_test_save.json"
        file_storage._FileStorage__file_path = test_path

        # Cancel test if test file already exists
        if os.path.exists(test_path):
            raise FileExistsError("Cannot create test file.")

        # Create and add bunch of objects
        objs = [BaseModel() for n in range(10)]
        for obj in objs:
            file_storage.new(obj)

        # Check that save() created a file
        file_storage.save()
        self.assertTrue(os.path.exists(test_path))

        # Remove test file
        os.remove(test_path)

    def test_reload(self):
        file_storage = FileStorage()
        test_path = "unittest_FileStorage_test_save.json"
        file_storage._FileStorage__file_path = test_path

        # Cancel test if test file already exists
        if os.path.exists(test_path):
            raise FileExistsError("Cannot create test file.")

        # Save a bunch of objects
        objs = [BaseModel() for n in range(10)]
        for obj in objs:
            file_storage.new(obj)
        file_storage.save()
        file_storage.reload()
        for obj in file_storage.all().values():
            self.assertIsInstance(obj, BaseModel)

        # Remove test file
        os.remove(test_path)

    def test_pep8(self):
        """Test PEP8."""
        style = pep8.StyleGuide(quiet=True)
        errors = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

if __name__ == '__main__':
    unittest.main()
