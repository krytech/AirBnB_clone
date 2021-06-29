#!/usr/bin/python3
""" Unittest BaseModel. """
import unittest
from ...models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test "BaseModel". """

    def test_init(self):
        """ Test "__init__". """
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)
        self.assertTrue(hasattr(bm, "id"))
        self.assertTrue(hasattr(bm, "created_at"))
        self.assertTrue(hasattr(bm, "updated_at"))

    def test_str(self):
        """ Test "__str__". """
        pass

    def test_save(self):
        """ Test "save". """
        pass

    def test_to_dict(self):
        """ Test "to_dict". """
        pass


if __name__ == '__main__':
    unittest.main()
