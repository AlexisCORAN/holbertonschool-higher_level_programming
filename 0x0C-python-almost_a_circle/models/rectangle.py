#!/usr/bin/python3
"""
This module defines the rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """A representation of Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instance of rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """returns getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of class"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns getter of height"""
        return self.__heigth

    @height.setter
    def height(self, value):
        """Sets height of class"""
        if type(value) is not int:
            raise TypeError("heigth must be an integer")
        if value <= 0:
            raise ValueError("heigth must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x of class"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y of class"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of class"""
        return self.__width * self.__height

    def display(self):
        """Prints a display of the rectangle"""
        for row in range(self.__height):
            for column in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """Returns string representation of the rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 sellf.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)
