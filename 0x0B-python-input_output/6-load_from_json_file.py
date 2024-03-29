#!/usr/bin/python3

"""
Create object from
JSON file
"""
from json import loads


def load_from_json_file(filename):
    """
    return created object
    from JSON file
    """

    stream = open(filename, mode='r', encoding='utf-8')
    with stream as fd:
        x = loads(fd.read())
        return x
