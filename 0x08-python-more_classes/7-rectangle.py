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

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        self.__width = value

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
        else:
            return (2 * (self.width + self.height))

    def __str__(self):
        """
        returned rectangle
        printed in #
        """

        strg = ''
        if self.width == 0 or self.height == 0:
            return strg
        for m in range(self.height):
            for n in range(self.width):
                strg += str(self.print_symbol)
            strg += '\n'
        return strg[0:-1]

    def __repr__(self):
        """
        returned a string that can be used
        to generate object of same class
        """

        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """
        return the message 'Bye Rectangle'
        whenever an instance of the class
        is deleted
        """

        cnt = "Bye rectangle..."
        print(cnt)
        Rectangle.number_of_instances -= 1
