#!/usr/bin/python3
"""
class module
defining a student
"""


class Student:
    """
    student class with
    public instance attribute
    and method and retrieve the
    dictionary representation
    """

    def __init__(self, first_name, last_name, age):
        """
        instantiate the instance
        attribute
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retieve the dictionary
        representation of a
        student instance
        """

        return vars(self)
