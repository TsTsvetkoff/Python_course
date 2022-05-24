import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('inflation.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')

    for row in plots:
        x.append(row[0])
        y.append(float(row[1]))

plt.bar(x, y, color='g', width=0.72, label="BG_Inflation")
plt.xlabel('Period')
plt.ylabel('Inflation rate')
plt.title('Monthly Bulgarian inflation 1999 - 2022')

plt.legend()
plt.show()
