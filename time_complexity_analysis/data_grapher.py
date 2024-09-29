import matplotlib.pyplot as plt
import csv

noise, dom, ffts, ffttimes, customs, customtimes = [], [], [], [], [], []

with open('data.csv', 'r') as csvfile:
    file = csv.reader(csvfile)

    for line in file:
        noise.append(line[0])
        dom.append(line[1])
        ffts.append(line[2])
        ffttimes.append(line[3])
        customs.append(line[4])
        customtimes.append(line[5])
    csvfile.close()

for my_list in noise, dom, ffts, ffttimes, customs, customtimes:
    my_list.pop(0) # name of column

noise = [round(float(value), 3) for value in noise]

fft_variance = [abs(float(ffts[i]) - float(dom[i])) for i in range(len(ffts))]
custom_variance = [abs(float(customs[i]) - float(dom[i])) for i in range(len(customs))]

fft_variance_average = []
custom_variance_average = []

for i in range(50):
    fft_variance_average.append(sum(fft_variance[i*30:(i*30)+30])/30)
    custom_variance_average.append(sum(custom_variance[i*30:(i*30)+30])/30)



plt.plot(noise, fft_variance, '.', label='FFT Variance')
plt.plot([i/1000 for i in range(50)], fft_variance_average, label='Average FFT Variance')
plt.plot(noise, custom_variance, '.', label='SFI Variance')
plt.plot([i/1000 for i in range(50)], custom_variance_average, label='Average SFI Variance')
plt.legend()
plt.show()