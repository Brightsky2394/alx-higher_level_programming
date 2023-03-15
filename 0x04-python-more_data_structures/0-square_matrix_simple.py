#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    if len(matrix) > 0:
        for item in matrix:
            storage = list(map(lambda i: i ** 2, item))
            new_matrix.append(storage)
    return new_matrix
