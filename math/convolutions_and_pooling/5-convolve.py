#!/usr/bin/env python3
"""Module that performs a convolution on images using multiple kernels"""
import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """Performs a convolution on images using multiple kernels"""
    m, h, w, c = images.shape
    kh, kw, _, nc = kernels.shape
    sh, sw = stride
    if padding == 'same':
        ph = ((h - 1) * sh + kh - h) // 2 + 1
        pw = ((w - 1) * sw + kw - w) // 2 + 1
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        ph, pw = padding
    padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw), (0, 0)),
                    mode='constant')
    oh = (h + 2 * ph - kh) // sh + 1
    ow = (w + 2 * pw - kw) // sw + 1
    output = np.zeros((m, oh, ow, nc))
    for i in range(oh):
        for j in range(ow):
            for k in range(nc):
                x = i * sh
                y = j * sw
                output[:, i, j, k] = np.sum(
                    padded[:, x:x + kh, y:y + kw, :] * kernels[:, :, :, k],
                    axis=(1, 2, 3))
    return output
