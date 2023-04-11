#!/usr/bin/python3

"""
function that returns True if the object
is an instance of a class that inherited
(directly or indirectly) from the
specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
    return true or false, if object
    is inherited from a specified
    class
    """

    x = isinstance(obj, a_class)
    y = x if not issubclass(a_class, obj.__class__) else False
    return y
