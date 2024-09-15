import csv

with open('data.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([0.0, 24.0, 24.0, 0.013, 24.0, 0.0032, 0])
    csvfile.close()