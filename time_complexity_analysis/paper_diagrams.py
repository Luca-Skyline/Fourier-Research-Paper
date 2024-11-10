import matplotlib.pyplot as plt
import random
import numpy as np

import fast_fourier_transform

def generate_magnitudes(total_mag, count):


    # Generate random float points
    points = sorted([random.uniform(0, total_mag) for _ in range(count-1)])

    if not points:
        return [total_mag]

    # Compute the gaps between the points and total
    magnitudes = [points[0]] + [points[i + 1] - points[i] for i in range(count - 2)] + [total_mag - points[-1]]

    return magnitudes


t = np.linspace(0, 1, 1024, endpoint=False) # time values
sine_wave1 = np.sin(2 * np.pi * 9.034 * t) # sine wave from random frequency (amplitude = 1)
sine_wave2 = 0.3 * np.sin(2 * np.pi * 23.111 * t)

sine_wave = sine_wave1 + sine_wave2

fourier_wave = [abs(value) for value in fast_fourier_transform.fft(sine_wave)]

plt.figure(figsize=(15, 4))
ax = plt.gca()
ax.set_ylim([-2, 2])

plt.plot(t, sine_wave1, color='red')
plt.xlabel('Time (s)')
plt.ylabel('Magnitude')

plt.show()

plt.figure(figsize=(15, 4))
ax = plt.gca()
ax.set_ylim([-2, 2])

plt.plot(t, sine_wave2, color='blue')
plt.xlabel('Time (s)')
plt.ylabel('Magnitude')

plt.show()

plt.figure(figsize=(15, 4))
ax = plt.gca()
ax.set_ylim([-2, 2])

plt.plot(t, sine_wave, color='purple')
plt.xlabel('Time (s)')
plt.ylabel('Magnitude')

plt.show()

plt.figure(figsize=(15, 4))

plt.plot(range(40), fourier_wave[0:40])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.show()

