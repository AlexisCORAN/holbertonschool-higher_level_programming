#!/usr/bin/python3
"""
This module defines the square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Representation of class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instance of class Square"""
        self.width = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                                                  self.x,
                                                  self.y,
                                                  self.height))

    @property
    def size(self):
        """Returns getter of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of square"""
        attrs = ["id", "size", "x", "y"]
        if 0 < len(args) <= 4:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        new_dic = {}
        new_dic["id"] = self.id
        new_dic["size"] = self.size
        new_dic["x"] = self.x
        new_dic["y"] = self.y
        return (new_dic)
