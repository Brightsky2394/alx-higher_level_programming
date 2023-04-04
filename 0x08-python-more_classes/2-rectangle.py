#!/usr/bin/python3
"""
A module made up of a rectangle class
with two instance variable width and
height.It has two public instance
methods
"""


class Rectangle:
    """
    rectangle class
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        returned the setter value
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        set the width value
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width

    @property
    def height(self):
        """
        returned the setter value
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        set the height value
        """

        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        returned the rectangle area
        """

        return (self.width * self.height)

    def perimeter(self):
        """
        returned the perimeter
        of the rectangle
        """

        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.width * self.height))
