#!/usr/bin/python3

"""
module testing the
instance of an object
"""


def is_same_class(obj, a_class):
    """
    return True if an object is an
    instance of a specified class
    """

    check = isinstance(obj, a_class)
    if check:
        return True
    return False
