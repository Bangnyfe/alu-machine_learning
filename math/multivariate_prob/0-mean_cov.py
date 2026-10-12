#!/usr/bin/env python3
"""Module for calculating the mean and covariance of a dataset."""

import numpy as np


def mean_cov(X):
    """Calculate the mean and covariance matrix of a dataset."""
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    n, d = X.shape

    if n < 2:
        raise ValueError("X must contain multiple data points")

    mean = np.mean(X, axis=0, keepdims=True)

    centered = X - mean

    cov = np.matmul(centered.T, centered) / (n - 1)

    return mean, cov
