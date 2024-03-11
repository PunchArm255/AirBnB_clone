#!/usr/bin/python3
"""
BaseModel module

This module defines the BaseModel class, which acts as a base class for
other models. It provides basic initialization, serialization and
deserialization methods for all models.
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class

    This class defines all common attributes/methods for other classes.
    It takes care of the initialization, serialization and
    deserialization of your future instances.

    Methods:
        __init__(*args, **kwargs): Initializes the BaseModel instance.
        __str__(): Returns a string representation of the BaseModel instance.
        save(): Updates the public instance attribute 'updated_at'
          with the current datetime.
        to_dict(): Returns a dictionary containing all keys/values
          of the instance's __dict__.

    Example Usage:
        >>> base_model = BaseModel()
        >>> print(base_model)
            [BaseModel] (unique_id) {'id': 'unique_id',
              'created_at': datetime, 'updated_at': datetime}
        >>> base_model.save()
        >>> print(base_model.updated_at)
            datetime
        >>> base_model_dict = base_model.to_dict()
        >>> print(base_model_dict)
            {'id': 'unique_id', 'created_at': 'datetime',
              'updated_at': 'datetime', '__class__': 'BaseModel'}
    """

    def __init__(self, *args, **kwargs):
        """Initialization of the BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        self.__dict__[key] = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """str representation of the BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        todict = self.__dict__.copy()
        todict['__class__'] = self.__class__.__name__
        todict['created_at'] = self.created_at.isoformat()
        todict['updated_at'] = self.updated_at.isoformat()
        return todict
