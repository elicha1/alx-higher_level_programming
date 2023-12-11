#!/usr/bin/python3
"""
Module containing the Base class.
"""

class Base:
    """
    The Base class for managing id attribute in all other classes.
    """

    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int): If provided, assign the public instance attribute id with
                      this argument value. Otherwise, increment __nb_objects
                      and assign the new value to the public instance attribute id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

