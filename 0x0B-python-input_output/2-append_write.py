#!/usr/bin/python3

"""
Module appending string
to the end of a text file
"""


def append_write(filename='', text=''):
    """
    append string to the end
    of a text file and return
    number of characters added
    """

    stream = open(filename, mode='at', encoding='utf-8')
    with stream as file_append:
        cnt = file_append.write(text)
        return cnt
