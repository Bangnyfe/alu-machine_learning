#!/usr/bin/env python3
"""Defines a function that concatenates two NumPy arrays."""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenates two matrices along a specified axis."""
    return np.concatenate((mat1, mat2), axis=axis)
