#!/usr/bin/python3
"""
Module reading a
test file
"""


def read_file(filename=''):
    """process the filename in the
    read mode
    """
    with open(filename, mode='rt', encoding='utf-8') as stream:
        for line in stream.read():
            print(line, end='')
