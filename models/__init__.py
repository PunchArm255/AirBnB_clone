#!/usr/bin/python3
"""
This code snippet creates a unique instance of the FileStorage
class and calls the reload() method on it. 
It then checks if the instance is not None and raises a ValueError
if it is. If an AttributeError occurs during the reload() method call,
it raises an AttributeError with the error message. 
This code snippet is used as an example of how to use 
the FileStorage class and handle potential errors.
"""
from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for your application
storage = FileStorage()
storage.reload()
