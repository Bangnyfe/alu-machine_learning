#!/usr/bin/env python3
"""Defines a function that performs element-wise operations."""


def np_elementwise(mat1, mat2):
    """Returns the sum, difference, product, and quotient of two matrices."""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
