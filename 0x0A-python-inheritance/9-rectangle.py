#!/usr/bin/python3

"""
BaseGeometry class with
public instance method
raising an exception
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    subclass Rectangle of the
    BaseGeometry class
    """

    def __init__(self, width, height):
        """
        instantiate the width and the
        height
        """

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        implementation of the
        area method
        """

        cnt = self.__width * self.__height
        return cnt

    def __str__(self):
        res = "[Rectangle] " + "{}" + "/" + "{}"
        return res.format(self.__width, self.__height)
