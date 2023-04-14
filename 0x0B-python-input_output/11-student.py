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

    def to_json(self, attrs=None):
        """
        retieve the dictionary
        representation of a
        student instance
        """

        stud_rep = vars(self)
        new_dict = {}

        if isinstance(attrs, list):
            for attr in attrs:
                if isinstance(attr, str) is False:
                    return stud_rep
                elif attr in stud_rep:
                    new_dict[attr] = stud_rep[attr]
            return new_dict
        else:
            return stud_rep

    def reload_from_json(self, json):
        """
        replaces all attributes
        of student instances
        """

        for name in json:
            value = json[name]
            setattr(self, name, value)
