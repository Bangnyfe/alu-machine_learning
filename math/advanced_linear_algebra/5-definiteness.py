#!/usr/bin/env python3
"""Defines a function that determines the definiteness of a matrix."""

import numpy as np


def definiteness(matrix):
    """Calculates and returns the definiteness of a matrix."""
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        return None

    if not np.allclose(matrix, matrix.T):
        return None

    eigenvalues = np.linalg.eigvalsh(matrix)
    tolerance = 1e-8

    if np.all(eigenvalues > tolerance):
        return "Positive definite"

    if np.all(eigenvalues >= -tolerance):
        return "Positive semi-definite"

    if np.all(eigenvalues < -tolerance):
        return "Negative definite"

    if np.all(eigenvalues <= tolerance):
        return "Negative semi-definite"

    return "Indefinite"
