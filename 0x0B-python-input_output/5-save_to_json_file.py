#!/usr/bin/python3
"""
write object to a
text file using JSON
representation
"""
from json import dumps


def save_to_json_file(my_obj, filename):
    """
    JSON way of writing
    object to text file
    """

    handle = open(filename, mode='wt', encoding='utf-8')
    with handle as fr:
        fr.write(dumps(my_obj))
