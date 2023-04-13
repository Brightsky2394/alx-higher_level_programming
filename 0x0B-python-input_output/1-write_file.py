#!/usr/bin/python3

"""
Module that write a string
to a text file
"""


def write_file(filename='', text=''):
    """
    write string to a text file
    and returns the number of
    characters written
    """

    control = open(filename, mode='wt', encoding='utf-8')
    with control as handle:
        cnt = handle.write(text)
        return cnt
