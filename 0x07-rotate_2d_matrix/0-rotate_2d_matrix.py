#!/usr/bin/python3
'''Rotate 2D Matrix'''


def rotate_2d_matrix(matrix):
    '''rotate a matrix by 90 degrees'''

    n = len(matrix)

    # Part 1: swapping i with j:=> M[i][j] => M[j][i]
    i = j = 0
    while i < n:
        j = i

        while j < n:
            c = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = c

            j += 1
        i += 1

    # Part 2: swapping columns
    for row in matrix:
        j = 0
        while j < n/2:
            row[j], row[n - 1 - j] = row[n - 1 - j], row[j]
            j += 1
