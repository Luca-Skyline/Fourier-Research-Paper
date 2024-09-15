import numpy as np


def fft(x):
    N = len(x)

    if N <= 1: # We have recursively reached the smallest level
        return x

    # Split by evens/odds and call recursively
    evens = fft(x[::2])
    odds = fft(x[1::2])

    # Combine results using twiddle factors
    T = [np.exp(-2j * np.pi * k / N) * odds[k] for k in range(N // 2)]

    return [evens[k] + T[k] for k in range(N // 2)] + [evens[k] - T[k] for k in range(N // 2)]
