#!/usr/bin/python3
import datetime
import unittest

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_id(self):
        self.assertTrue(hasattr(self.model, "id"))

    def test_created_at(self):
        self.assertTrue(hasattr(self.model, "created_at"))

    def test_updated_at(self):
        self.assertTrue(hasattr(self.model, "updated_at"))

    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        dict_obj = self.model.to_dict()
        self.assertEqual(dict_obj["__class__"], "BaseModel")
        self.assertIsInstance(dict_obj["created_at"], str)
        self.assertIsInstance(dict_obj["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
