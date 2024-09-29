import numpy as np

def fft(x):
    N = len(x)

    # base case
    if N <= 1:
        return x

    # Split by evens/odds and call recursively
    evens = fft(x[::2])
    odds = fft(x[1::2])

    # Combine results using a miniature DFT
    X = [np.exp(-2j * np.pi * k / N) * odds[k] for k in range(N // 2)]
    X = [evens[k] + X[k] for k in range(N // 2)] + [evens[k] - X[k] for k in range(N // 2)]

    return X
