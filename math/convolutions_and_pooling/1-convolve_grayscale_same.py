#!/usr/bin/env python3
"""Module for performing same convolutions on grayscale images."""

import numpy as np


def convolve_grayscale_same(images, kernel):
    """Perform a same convolution on grayscale images."""
    m, h, w = images.shape
    kh, kw = kernel.shape

    pad_h = (kh - 1) // 2
    pad_h_extra = kh - 1 - pad_h
    pad_w = (kw - 1) // 2
    pad_w_extra = kw - 1 - pad_w

    padded_images = np.pad(
        images,
        ((0, 0), (pad_h, pad_h_extra), (pad_w, pad_w_extra)),
        mode='constant'
    )

    output = np.zeros((m, h, w))

    for i in range(h):
        for j in range(w):
            output[:, i, j] = np.sum(
                padded_images[:, i:i + kh, j:j + kw] * kernel,
                axis=(1, 2)
            )

    return output
