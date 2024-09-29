import custom_algorithm         # contains custom algorithm
import fast_fourier_transform   # contains my FFT algorithm, based on Cooley-Tukey

import numpy as np
import random
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


dominant_min = 1.0     # Min and max of the algorithms' "target" value: the frequency with the largest magnitude
dominant_max = 12.0
trials = 30             # Repeat each generation of random data this many times with identical input parameters
max_frequencies = 4     # In addition to the dominant frequency, how many waves can we add to get our THD
duration = 1            # Seconds of sample generated

sampling_rates = []
fft_times = []
custom_times = []

for i in range(10):
    sampling_rate = 2 ** (i+6)
    print(sampling_rate)

    for j in range(trials):
        dominant_frequency = random.uniform(dominant_min, dominant_max)  # random frequency
        t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)  # time values
        sine_wave = np.sin(2 * np.pi * dominant_frequency * t)  # sine wave from random frequency (amplitude = 1)

        #print(sine_wave)

        t1 = time.time()
        fft_result = fast_fourier_transform.fft(sine_wave)  # transform into list of amplitudes
        # Find dominant frequency from list:
        dominant_amplitude = 0
        for x, m in enumerate(fft_result[:(int(sampling_rate/2))]):
            if abs(m) > dominant_amplitude:
                dominant_amplitude = abs(m)
                fft_guess = x
        t1 = time.time() - t1

        t2 = time.time()
        custom_result = custom_algorithm.estimate_dominant_frequency(sine_wave)    # returns single value
        t2 = time.time() - t2

        sampling_rates.append(sampling_rate)
        fft_times.append(t1)
        custom_times.append(t2)


fft_times = np.array(fft_times)
custom_times = np.array(custom_times)
sampling_rates = np.array(sampling_rates)

# FIND N LOG N REGRESSION
def n_log_n_model(x, a, b):
    x = np.array(x, dtype=np.float64)
    return a * x * np.log(x) + b
params, covariance = curve_fit(n_log_n_model, sampling_rates, fft_times)
a, b = params
y_fit = n_log_n_model(sampling_rates, a, b)

residuals = fft_times - y_fit
ss_res = np.sum(residuals**2)  # Sum of squares of residuals
ss_tot = np.sum((fft_times - np.mean(fft_times))**2)  # Total sum of squares
r_squared = 1 - (ss_res / ss_tot)

# FIND LINEAR REGRESSIONS AND R^2 VALUES
custom_x = sampling_rates.reshape((-1, 1))
model = LinearRegression()
model.fit(custom_x, custom_times)
y_pred = model.predict(custom_x)
custom_r2 = r2_score(custom_times, y_pred)

custom_

#plt.plot(np.unique(sampling_rates), np.poly1d(np.polyfit(sampling_rates, custom_times, 1))(np.unique(sampling_rates)), label='Linear Regression')
plt.plot(sampling_rates, y_pred, label=f'Linear Regression: R^2={r2}')
plt.plot(np.unique(sampling_rates), np.poly1d(np.polyfit(sampling_rates, fft_times, 1))(np.unique(sampling_rates)), label='FFT Linear Regression')
plt.plot(sampling_rates, y_fit, label=f'NlogN Regression: R^2={r_squared}')
plt.plot(sampling_rates, custom_times, 'o', label='Custom Algorithm')
plt.plot(sampling_rates, fft_times, 'o', label='FFT Algorithm')

plt.legend()
plt.xscale("log")
plt.show()