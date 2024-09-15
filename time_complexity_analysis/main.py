# Luca DalCanto 09/15/2024

# The objective of this code is five-fold:
#   - Define a Cooley-Tukey FFT which takes in amplitude-time data and transforms it into frequency-magnitude data
#   - Define a custom algorithm which attempts to estimate the dominant frequency of amplitude-time data
#   - Generate random data according to the input parameters, then feed it into both of the algorithms
#     those algorithms and compare performance in time & accuracy
#   - Automate the input parameters to test the independent variable automatically and with many variations
#   - Record data and display results

import random
import dominant_frequency_estimator     # contains custom algorithm
import fast_fourier_transform           # contains my FFT algorithm, based on Cooley-Tukey

# Independent Variable (Total Harmonic Distortion) Testing Range
THD_min = 0             # Begin with testing pure waves
THD_max = 0.5           # Increase distortion until it's this fraction of the magnitude of the dominant frequency
THD_step = 0.01         # Increase THD in steps of 0.01

# Other parameters
dominant_min = 1.01     # Min and max of the algorithms' "target" value: the frequency with the largest magnitude
dominant_max = 39.9
trials = 30             # Repeat each generation of random data this many times with identical input parameters
max_frequencies = 4     # In addition to the dominant frequency, how many waves can we add to get our THD

# GENERATE AND TEST DATA
THD = THD_min
while THD <= THD_max:
    for i in range(trials):  # repeat with same THD this many times
        pass
        # generate random wave data
        # dominant_frequency = __

        # run & time FFT
        # run & time my algorithm

        # save data:
        # - THD
        # - Actual Dominant Frequency
        # - FFT and custom estimations of ^
        # - FFT and custom times
        # - number of minor frequencies
        # -

    THD += THD_step

# ANALYZE, SAVE, AND DISPLAY DATA


# for generating magnitudes of multiple waves to add up to a total magnitude
def generate_floats(total_mag, count):
    # Generate random float points
    points = sorted([random.uniform(0, total_mag) for _ in range(count - 1)])

    # Compute the gaps between the points and total
    magnitudes = [points[0]] + [points[i + 1] - points[i] for i in range(count - 2)] + [total_mag - points[-1]]

    return magnitudes
