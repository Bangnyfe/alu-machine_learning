#!/usr/bin/env python3
"""Defines a function that calculates the adjugate matrix."""


def adjugate(matrix):
    """Calculates and returns the adjugate matrix of a matrix."""
    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    size = len(matrix)

    if not all(len(row) == size for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if size == 1:
        return [[1]]

    def determinant(mat):
        """Calculates the determinant of a square matrix."""
        if len(mat) == 1:
            return mat[0][0]

        if len(mat) == 2:
            return mat[0][0] * mat[1][1] - \
                mat[0][1] * mat[1][0]

        total = 0
        for col in range(len(mat)):
            submatrix = [
                [mat[row][j] for j in range(len(mat)) if j != col]
                for row in range(1, len(mat))
            ]
            sign = 1 if col % 2 == 0 else -1
            total += sign * mat[0][col] * determinant(submatrix)

        return total

    cofactor_matrix = []

    for i in range(size):
        row = []

        for j in range(size):
            submatrix = [
                [matrix[r][c] for c in range(size) if c != j]
                for r in range(size) if r != i
            ]

            value = determinant(submatrix)

            if (i + j) % 2 == 1:
                value = -value

            row.append(value)

        cofactor_matrix.append(row)

    return [
        [cofactor_matrix[j][i] for j in range(size)]
        for i in range(size)
    ]
