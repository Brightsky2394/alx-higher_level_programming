#!/usr/bin/python3

"""
BaseGeometry class with
public instance method
raising an exception
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    square class a
    subclass to rectangle
    class
    """

    def __init__(self, size):
        """
        instantiate the size parameter
        """
        super.integer_validator("size", size)
        self.size = size
        super.__init__(size, size)

    def area(self, size):
        """
        compute and return val
        of area
        """

        val = self.__size * self.__size
        return val

    def __str__(self):
        """
        return an object in a
        more readable form
        """

        cnt = "[{}] " + "{}" + "/" + "{}"
        return cnt.format(self.__class__.__name__, self.__size, self.__size)
