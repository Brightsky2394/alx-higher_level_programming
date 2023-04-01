#!/usr/bin/python3

def add_integer(a, b=98):

    """
    Add two integer number together. If argument is float,
    cast it to integer and add the two number together
    with the result return. If argument is not integer
    or float raise TypeError exception
    """

    if isinstance(a, int or float):
        num1 = int(a)
    if isinstance(b, int or float):
        num2 = int(b)
    if isinstance(num1 and num2, int):
        cnt = num1 + num2
        return cnt
