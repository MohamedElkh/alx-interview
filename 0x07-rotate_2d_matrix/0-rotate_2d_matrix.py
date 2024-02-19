#!/usr/bin/python3
"""this func to define  rotates an nxn 2D matrix 90 degree"""


def rotate_2d_matrix(matrix):
    """this func to rotate 2d square matrix 90 degrees
    args:
        matrix: square matrix
    """
    n = len(matrix)

    for x in range(n):
        for k in range(x):
            tmp = matrix[x][k]

            matrix[x][k] = matrix[k][x]
            matrix[k][x] = tmp

    for x in range(n):
        for k in range(int(n / 2)):
            tmp = matrix[x][k]

            matrix[x][k] = matrix[x][n-1-k]
            matrix[x][n-1-k] = tmp
