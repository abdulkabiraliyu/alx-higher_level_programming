#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """a function that prints a matrix of integers."""

    if not matrix:
        print()
    else:
        for row in range(len(matrix)):
            for item in range(len(matrix[row])):
                if item != len(matrix[row]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}".format(matrix[row][item]), end=endspace)
            print()
