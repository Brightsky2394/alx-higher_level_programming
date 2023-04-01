#!/usr/bin/python3

def add_integer(a, b=98):

    """
    Add two integer number together. If argument is float,
    cast it to integer and add the two number together
    with the result return. If argument is not integer
    or float raise TypeError exception
    """

    if isinstance(a, (float, int)) is True:
        num1 = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, (float, int)) is True:
        num2 = int(b)
    else:
        raise TypeError("b must be an integer")
    cnt = num1 + num2
    return cnt
