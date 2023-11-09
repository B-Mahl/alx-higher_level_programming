#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for row in range(len(new_matrix)):
        for i in range(len(new_matrix[row])):
            new_matrix[row][i] = new_matrix[row][i] ** 2
    return new_matrix
