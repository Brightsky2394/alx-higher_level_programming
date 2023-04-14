#!/usr/bin/python3

"""
Module with list of lists
of integers representing
pascal triangle
"""


def pascal_triangle(n):
    """
    return list of lists of
    integers as a pascal triangle
    """

    my_list = []
    if n <= 0:
        return my_list

    array = [[1]]
    while (len(array)) < n:
        l_trm = array[-1]
        n_lst = [1]
        for j in range(len(l_trm) - 1):
            n_lst.append(l_trm[j] + l_trm[j + 1])
        n_lst.append(1)
        array.append(n_lst)
    return array
