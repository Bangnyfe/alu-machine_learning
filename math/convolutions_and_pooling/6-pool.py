#!/usr/bin/env python3
"""Module for performing pooling on images."""

import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """Perform max or average pooling on images."""
    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride

    output_h = (h - kh) // sh + 1
    output_w = (w - kw) // sw + 1

    output = np.zeros((m, output_h, output_w, c))

    for i in range(output_h):
        for j in range(output_w):
            window = images[
                :,
                i * sh:i * sh + kh,
                j * sw:j * sw + kw,
                :
            ]

            if mode == 'max':
                output[:, i, j, :] = np.max(
                    window, axis=(1, 2)
                )
            elif mode == 'avg':
                output[:, i, j, :] = np.mean(
                    window, axis=(1, 2)
                )
            else:
                raise ValueError("mode must be 'max' or 'avg'")

    return output
