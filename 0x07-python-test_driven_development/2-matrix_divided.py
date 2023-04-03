#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    matrix must be list of lists of integers/floats.
    If it is not a list raise TypeError exception.
    When div is 0 raise a ZeroDivisionError.
    If the row of each sub-list is not same size
    raise a TypeError exception and finally returned
    the new_matrix
    """
    if isinstance(div, (float, int)) is False:
        raise TypeError("div must be a number")
    elif div is 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(matrix, list) is False or len(matrix) is 0:
        raise TypeError("matrix must be matrix (list of lists)\
                of integers/floats")
    else:
        for term in matrix:
            if isinstance(term, list) is False:
                raise TypeError("matrix must be matrix (list of lists)\
                        of integers/floats")
            else:
                for el in term:
                    if isinstance(el, (float, int)) is False:
                        raise TypeError("matrix must be matrix (list of lists)\
                                of integers/floats")
        row_len = len(matrix[0])
        for i in range(len(matrix)):
            if len(matrix[i]) != row_len:
                raise TypeError("Each row of the matrix must\
                        have the same size")
        new_matrix = [[round((elem / div), 2) for elem in j] for j in matrix]
    return new_matrix
