#!/usr/bin/python3
""" unit test for bases """

import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        mymodel = BaseModel()
        models.storage.new(mymodel)
        self.assertIn('BaseModel.' + mymodel.id, models.storage.all().keys())

    def test_save(self):
        mymodel = BaseModel()
        models.storage.new(mymodel)
        models.storage.save()
        self.assertTrue(os.path.exists('file.json'))
        with open('file.json', 'r') as f:
            self.assertIn('BaseModel.' + mymodel.id, f.read())

    def test_reload(self):
        mymodel = BaseModel()
        models.storage.new(mymodel)
        models.storage.save()
        models.storage.reload()
        self.assertIn('BaseModel.' + mymodel.id, models.storage.all().keys())


if __name__ == '__main__':
    unittest.main()
