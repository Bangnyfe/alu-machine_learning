#!/usr/bin/env python3
"""Module for the multivariate normal distribution."""

import numpy as np


class MultiNormal:
    """Represents a multivariate normal distribution."""

    def __init__(self, data):
        """Initialize the mean and covariance of the distribution."""
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)

        centered = data - self.mean

        self.cov = np.matmul(centered, centered.T) / (n - 1)

    def pdf(self, x):
        """Calculate the PDF at a given data point."""
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        d = self.mean.shape[0]

        if x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))

        difference = x - self.mean

        determinant = np.linalg.det(self.cov)
        inverse = np.linalg.inv(self.cov)

        exponent = -0.5 * np.matmul(
            np.matmul(difference.T, inverse), difference
        )

        pdf_value = (
            1 / (((2 * np.pi) ** (d / 2)) * (determinant ** 0.5))
        ) * np.exp(exponent[0, 0])

        return pdf_value
