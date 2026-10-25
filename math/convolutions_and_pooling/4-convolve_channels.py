#!/usr/bin/env python3
"""Module for performing convolutions on images with channels."""

import numpy as np


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    """Perform a convolution on images with channels."""
    m, h, w, c = images.shape
    kh, kw, kc = kernel.shape
    sh, sw = stride

    if c != kc:
        raise ValueError("Image and kernel channels must match")

    if padding == 'same':
        output_h = int(np.ceil(h / sh))
        output_w = int(np.ceil(w / sw))

        pad_h = max((output_h - 1) * sh + kh - h, 0)
        pad_w = max((output_w - 1) * sw + kw - w, 0)

        pad_top = pad_h // 2
        pad_bottom = pad_h - pad_top
        pad_left = pad_w // 2
        pad_right = pad_w - pad_left

    elif padding == 'valid':
        pad_top = pad_bottom = 0
        pad_left = pad_right = 0

    else:
        ph, pw = padding
        pad_top = pad_bottom = ph
        pad_left = pad_right = pw

    padded_images = np.pad(
        images,
        (
            (0, 0),
            (pad_top, pad_bottom),
            (pad_left, pad_right),
            (0, 0)
        ),
        mode='constant'
    )

    padded_h, padded_w = padded_images.shape[1:3]
    output_h = (padded_h - kh) // sh + 1
    output_w = (padded_w - kw) // sw + 1

    output = np.zeros((m, output_h, output_w))

    for i in range(output_h):
        for j in range(output_w):
            output[:, i, j] = np.sum(
                padded_images[
                    :,
                    i * sh:i * sh + kh,
                    j * sw:j * sw + kw,
                    :
                ] * kernel,
                axis=(1, 2, 3)
            )

    return output
