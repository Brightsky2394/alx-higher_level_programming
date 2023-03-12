#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_num = min(my_list)
    for y in my_list:
        if y > max_num:
            max_num = y
    return max_num
