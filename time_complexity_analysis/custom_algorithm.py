# custom method which is intended to estimate ONLY the main frequency of the input data
# def estimate_dominant_frequency(x):
#     crosses = 0
#     for i in range(int((len(x)/2))):
#         if x[i] * x[i + 1] < 0:  # numbers switch positive to negative or negative to positive
#             crosses += 1
#     return crosses

import numpy as np
def estimate_dominant_frequency(x):
    amplitude = (max(x) - min(x)) / 2
    cross_slopes_sum = 0
    crosses = 0
    length = len(x)
    for i in range(length-1):
        if x[i] * x[i + 1] < 0:  # numbers switch positive to negative or negative to positive
            cross_slopes_sum += ((abs(x[i]-x[i+1]) * length)  # slope between 2 points
                                 + (50 * (abs(x[i]-x[i+1]) ** 3)))  # extra compensation if points are far apart
            crosses += 1

    return (cross_slopes_sum / crosses) / (amplitude * np.pi * 2)

