#!/usr/bin/python3

"""
module defining a rectangle class
with instance value width and
height
"""


class Rectangle:
    """
    initiate the instance
    variable width and height
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        retrieve the width value
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        set the value of width
        """

        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        retrieve the value of height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        set the value of height
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
