#!/usr/bin/python3

"""
Module with JSON
representation of
an object
"""
from json import dumps


def to_json_string(my_obj):
    """
    return the JSON representation
    of an object
    """

    res = dumps(my_obj)
    return res
