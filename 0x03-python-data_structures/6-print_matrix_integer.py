#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for elems in matrix:
            x = 1
            length = len(elems)
            for elem in elems:
                if x == length:
                    print("{:d}".format(elem), end='')
                else:
                    print("{:d}".format(elem), end=' ')

                x += 1
            print()
