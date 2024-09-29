# Luca DalCanto 09/15/2024

# The objective of this code is five-fold:
#   - Define a Cooley-Tukey FFT which takes in amplitude-time data and transforms it into frequency-magnitude data
#   - Define a custom algorithm which attempts to estimate the dominant frequency of amplitude-time data
#   - Generate random data according to the input parameters, then feed it into both of the algorithms
#     those algorithms and compare performance in time & accuracy
#   - Automate the input parameters to test the independent variable automatically and with many variations
#   - Record data and display results

import random
import numpy as np
import time
import csv
import custom_algorithm         # contains custom algorithm
import fast_fourier_transform   # contains my FFT algorithm, based on Cooley-Tukey

# Independent Variable (Total Harmonic Distortion) Testing Range
SNR_min = 0             # Begin with testing pure waves
SNR_max = 0.05           # Increase distortion until it's this fraction of the magnitude of the dominant frequency
SNR_step = 0.001         # Increase SNR in steps of 0.01

# Other parameters
dominant_min = 1.0     # Min and max of the algorithms' "target" value: the frequency with the largest magnitude
dominant_max = 40.0
trials = 30             # Repeat each generation of random data this many times with identical input parameters
max_frequencies = 4     # In addition to the dominant frequency, how many waves can we add to get our SNR
sampling_rate = 512     # Samples per second
duration = 1            # Seconds of sample generated

# CSV Storage
filename = 'data.csv'   # Fields:   'SNR', 'Dominant Frequency', 'FFT Estimation', 'Custom Estimation',
                        #           'FFT Time', 'Custom Time', 'Frequency Count'
                        
# for generating magnitudes of multiple waves (with different frequencies) to add up to a total magnitude
def generate_magnitudes(total_mag, count):


    # Generate random float points
    points = sorted([random.uniform(0, total_mag) for _ in range(count-1)])

    if not points:
        return [total_mag]

    # Compute the gaps between the points and total
    magnitudes = [points[0]] + [points[i + 1] - points[i] for i in range(count - 2)] + [total_mag - points[-1]]

    return magnitudes






# GENERATE AND TEST DATA
SNR = SNR_min
while SNR <= SNR_max:
    for i in range(trials):  # repeat with same SNR this many times

        my_row = [SNR] # save data from this trial

        # generate random wave data
        dominant_frequency = random.uniform(dominant_min, dominant_max) # random frequency
        t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False) # time values
        sine_wave = np.sin(2 * np.pi * dominant_frequency * t) # sine wave from random frequency (amplitude = 1)

        frequency_count = random.randint(1, max_frequencies)
        noise = generate_magnitudes(SNR, frequency_count)
        for amplitude in noise:
            t_freq = random.uniform(dominant_min, dominant_max)
            sine_wave += amplitude * np.sin(2 * np.pi * t_freq * t)

        my_row.append(dominant_frequency)

        # -- RUN & TIME FFT --
        t1 = time.time()
        fft_result = fast_fourier_transform.fft(sine_wave)  # transform into list of amplitudes
        # Find dominant frequency from list:
        dominant_amplitude = 0
        for x, m in enumerate(fft_result[:(int(sampling_rate/2))]):
            if abs(m) > dominant_amplitude:
                dominant_amplitude = abs(m)
                fft_guess = x
        t1 = time.time() - t1

        my_row.append(fft_guess)
        my_row.append(t1)

        # -- RUN & TIME My Algorithm --
        t2 = time.time()
        custom_result = custom_algorithm.estimate_dominant_frequency(sine_wave)    # returns single value
        t2 = time.time() - t2

        my_row.append(custom_result)
        my_row.append(t2)
        my_row.append(frequency_count)

        # -- APPEND DATA --
        with open('data.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(my_row)
            csvfile.close()

        print(my_row)

    SNR += SNR_step
