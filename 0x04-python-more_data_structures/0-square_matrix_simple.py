#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return matrix

    square_matrix = matrix.copy()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            square_matrix[i][j] = matrix[i][j] * matrix[i][j]

    return square_matrix
