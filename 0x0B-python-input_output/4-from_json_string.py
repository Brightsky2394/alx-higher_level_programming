#!/usr/bin/python3

"""
object represented
by a JSON string
"""
from json import loads


def from_json_string(my_str):
    """
    return object represented
    by a JSON string
    """

    res = loads(my_str) if True else False
    return res
