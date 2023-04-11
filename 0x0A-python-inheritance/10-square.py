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

        Rectangle.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
