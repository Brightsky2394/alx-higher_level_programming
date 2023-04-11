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
