#!/usr/bin/python3
"""
class BaseModel that defines all common
attributes/methods for other classes
take care of the initialization, serialization and
deserialization of your future instances
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """Initialization of the BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """str representation of the BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        todict = self.__dict__.copy()
        todict['__class__'] = self.__class__.__name__
        todict['created_at'] = self.created_at.isoformat()
        todict['updated_at'] = self.updated_at.isoformat()
        return todict
