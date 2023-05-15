#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("{:d}".format(matrix[i][j]), end='')
            if j == (len(matrix[0]) - 1):
                print(end='$\n')
            else:
                print(end=' ')

    if len(matrix[0]) == 0:
        print("$")
