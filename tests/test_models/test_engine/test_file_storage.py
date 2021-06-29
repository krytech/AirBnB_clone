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
        pass
    """
        try:
            os.remove("file.json")
        except Exception:
            pass
        try:
            with open() as file:

        except FileNotFoundError:
            pass
    """

    def test_reload(self):
        pass

    def test_pep8(self):
        """Test PEP8."""
        style = pep8.StyleGuide(quiet=True)
        errors = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

if __name__ == '__main__':
    unittest.main()
