#!/usr/bin/env python3
"""Defines a function that calculates the determinant of a matrix."""


def determinant(matrix):
    """Calculates and returns the determinant of a matrix."""
    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if matrix == [[]]:
        return 1

    size = len(matrix)
    if not all(len(row) == size for row in matrix):
        raise ValueError("matrix must be a square matrix")

    if size == 1:
        return matrix[0][0]

    if size == 2:
        return matrix[0][0] * matrix[1][1] - \
            matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(size):
        minor = [
            [matrix[row][j] for j in range(size) if j != col]
            for row in range(1, size)
        ]
        sign = 1 if col % 2 == 0 else -1
        det += sign * matrix[0][col] * determinant(minor)

    return det
