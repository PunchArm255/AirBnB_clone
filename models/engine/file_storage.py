#!/usr/bin/python3
"""
    This module defines the FileStorage class,
        which provides mechanisms for serializing
        and deserializing objects to and from a
        JSON file..
"""
import json
import os
# from models.user import User #avoid unused imports
# from models.base_model import BaseModel #avoid circular


class FileStorage:
    """
    A class that provides methods for storing and
        retrieving objects in a JSON file.
    This class provides a simple key-value store
        where the key is the object's class
        name and its id, and the value is the object itself.

    Attributes:
        __file_path (str): The path to the JSON file that
            will be used to store the objects.
        __objects (dict): A dictionary that stores the objects.
            The keys are the objects' class names and ids,
            and the values are the objects.

    Methods:
        all(self): Returns a copy of the dictionary __objects.
        new(self, obj): Adds the obj to the __objects dictionary, using the key
            <obj class name>.id.
        save(self): Serializes the __objects dictionary to the JSON file
            located at __file_path.
        reload(self): Deserializes the JSON file located at __file_path and
            loads it into the __objects dictionary.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a copy of the __objects dictionary.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds the given object to the __objects dictionary using the key
        <obj class name>.id.

        Args:
            obj: The object to be added.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the __objects dictionary to a JSON file
            located at __file_path.
        """
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file located at __file_path and
            loads it into the __objects dictionary.
        If the file does not exist,
            the __objects dictionary is left unchanged.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                deserialized_objects = json.load(file)
                for key, value in deserialized_objects.items():
                    class_name, obj_id = key.split('.')
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
