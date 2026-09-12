#!/usr/bin/env python3
"""Defines a function that calculates the shape of a matrix."""


def matrix_shape(matrix):
    """Calculates the shape of a matrix."""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] if matrix else []
    return shape
