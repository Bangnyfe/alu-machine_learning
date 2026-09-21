#!/usr/bin/env python3
"""Calculates the integral of a polynomial."""


def poly_integral(poly, C=0):
    """Return the integral of a polynomial."""
    if not isinstance(poly, list) or not poly:
        return None

    if not isinstance(C, int):
        return None

    if not all(isinstance(coef, (int, float)) for coef in poly):
        return None

    if len(poly) == 1 and poly[0] == 0:
        return [C]

    integral = [C]

    for power, coef in enumerate(poly):
        value = coef / (power + 1)

        if value.is_integer():
            value = int(value)

        integral.append(value)

    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
