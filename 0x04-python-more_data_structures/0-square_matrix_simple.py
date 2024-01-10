#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """function that computes the square value of all integers of a matrix"""

    if matrix:
        new_matrix = list(map(lambda x: [i**2 for i in x], matrix))
        return (new_matrix)
