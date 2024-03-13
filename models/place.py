#!/usr/bin/python3
"""
Module for the Place class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of place.
        description (str): The description of place.
        number_rooms (int): The number of rooms of place.
        number_bathrooms (int): The number of bathrooms of place.
        max_guest (int): The max number of guests in place.
        price_by_night (int): The price by night of place.
        latitude (float): The latitude of place.
        longitude (float): The longitude of place.
        amenity_ids (list): A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
