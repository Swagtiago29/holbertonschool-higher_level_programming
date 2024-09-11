#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    niu_matrix = [i[:] for i in matrix]
    for row in range(len(matrix)):
        for f in  range(len(matrix[row])):
          niu_matrix[row][f] = matrix[row][f] * matrix[row][f]
    return niu_matrix
