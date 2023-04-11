#!/usr/bin/python3

"""
list of attributes and
methods of an object.
"""


def lookup(obj):
    """
    return list of all methods and
    attributes of an object
    """

    res = [items for items in dir(obj)]
    return res
