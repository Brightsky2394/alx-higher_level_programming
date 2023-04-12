#!/usr/bin/python3

"""
BaseGeometry class with
public instance method
raising an exception
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    square class a subclass
    to the rectangle class
    """

    def __init__(self, size):
        """
        instantiate size
        """

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        compute and return the
        area of square
        """

        val = self.__size * self.__size
        return val

    def __str__(self):
        """
        return object in a
        more readable form
        """

        cnt = '[{}] ' + '{}' + '/' + "{}"
        return cnt.format(self.__class__.__name__, self.__size, self.__self)
