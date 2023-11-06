#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in range(len(row)):
            end_chr = ' ' if element + 1 != len(row) else ''
            print('{:d}'.format(row[element]), end=end_chr)
        print()
