#!/usr/bin/env python3
"""Calculates the derivative of a polynomial."""


def poly_derivative(poly):
    """Return the derivative of a polynomial."""
    if not isinstance(poly, list) or not poly:
        return None

    if not all(isinstance(coef, (int, float)) for coef in poly):
        return None

    if len(poly) == 1:
        return [0]

    derivative = []

    for power in range(1, len(poly)):
        derivative.append(poly[power] * power)

    while len(derivative) > 1 and derivative[-1] == 0:
        derivative.pop()

    return derivative
