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
