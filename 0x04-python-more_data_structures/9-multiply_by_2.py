#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary
    for i, j in a_dictionary.items():
        new_dict[i] = 2 * j
    return new_dict
