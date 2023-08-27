#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.

    Attributes:
        city_id (str): The city id.
        name (str): The name of the city.
    """

    def __init__(self, *args, **kwargs):
        """
            Initialize class user with kwargs
            Args:
                *args(positional arg): strings
                **kwargs(keyword arg): dictionary
        """
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.name = ""
