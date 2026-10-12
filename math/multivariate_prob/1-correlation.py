#!/usr/bin/env python3
"""Module for calculating a correlation matrix."""

import numpy as np


def correlation(C):
    """Calculate the correlation matrix from a covariance matrix."""
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    if C.ndim != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    stddev = np.sqrt(np.diag(C))

    correlation_matrix = C / np.outer(stddev, stddev)

    return correlation_matrix
