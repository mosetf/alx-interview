#!/usr/bin/python3
"""
2 dimentional matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n by n 2D matrix in place.
    """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    rows = len(matrix)
    cols = len(matrix[0])
    if not all(map(lambda x: len(x) == cols, matrix)):
        return
    q, t = 0, rows - 1
    for w in range(rows * cols):
        if w % rows == 0:
            matrix.append([])
        if t == -1:
            t = rows - 1
            q += 1
        matrix[-1].append(matrix[t][q])
        if q == cols - 1 and t >= -1:
            matrix.pop(t)
        t -= 1
