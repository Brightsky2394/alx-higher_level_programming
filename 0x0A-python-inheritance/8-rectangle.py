#!/usr/bin/python3

"""
BaseGeometry class with
public instance method raising
an Exception
"""


class BaseGeometry:
    """
    BaseGeometry class
    """

    def area(self):
        """
        raises an Exception
        """

        message = "area() is not implemented"
        raise Exception(message)

    def integer_validator(self, name, value):
        """
        validate the value
        supplied
        """

        if isinstance(value, int) is False:
            message1 = "{} must be an integer"
            raise TypeError(message1.format(name))
        elif value <= 0:
            message2 = "{} must be greater than 0"
            raise ValueError(message2.format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """

    def __init__(self, width, height):
        """
        instantiate the width and
        height parameter
        """

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
