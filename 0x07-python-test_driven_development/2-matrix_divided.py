#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    each element of the matrix is divided by div and
    return a new matrix, with the results in 2
    precisionnumbers. If div not is a number raise
    TypeError or ZeroDivisionError if div is 0.
    If matrix not is a list of lists return TypeError.
    If some sub-list aren't a list return TypeError.
    If some element of some sub-list aren't integer
    or float number return TypeError
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a  matrix (list of lists)\
                of integers/floats")
    else:
        for term in matrix:
            if type(term) is not list:
                raise TypeError("matrix must be matrix (list of lists)\
                        of integers/floats")
            else:
                for el in term:
                    if type(el) not in (int, float):
                        raise TypeError("matrix must be matrix (list of lists)\
                                of integers/floats")
        row_len = len(matrix[0])
        for i in range(len(matrix)):
            if len(matrix[i]) is not row_len:
                raise TypeError("Each row of the matrix must\
                        have the same size")
        new_matrix = [[round((elem / div), 2) for elem in j] for j in matrix]
    return new_matrix
