#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_init(self):
        """Test the initialization of BaseModel"""
        model_no_args = BaseModel()
        self.assertIsNotNone(model_no_args.id)
        self.assertIsInstance(model_no_args.created_at, datetime)
        self.assertIsInstance(model_no_args.updated_at, datetime)

    def test_str(self):
        """Test the string representation of BaseModel"""
        model_default = BaseModel()
        expected_default_str = "[BaseModel] ({}) {}".format(
            model_default.id, model_default.__dict__)
        self.assertEqual(str(model_default), expected_default_str)

    def test_save(self):
        """Test the save method of BaseModel"""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)
        self.assertIsInstance(model.updated_at, datetime)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel"""
        model_default = BaseModel()
        expected_default_dict = {
            'id': model_default.id,
            '__class__': 'BaseModel',
            'created_at': model_default.created_at.isoformat(),
            'updated_at': model_default.updated_at.isoformat()
        }
        self.assertDictEqual(model_default.to_dict(), expected_default_dict)


if __name__ == '__main__':
    unittest.main()
