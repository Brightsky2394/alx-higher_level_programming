#!/usr/bin/python3

from json import dumps
"""
Module with JSON
representation of
an object
"""


def to_json_string(my_obj):
    """
    return the JSON representation
    of an object
    """

    res = dumps(my_obj) if True else False
    return res
