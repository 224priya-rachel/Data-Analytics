import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('iris.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')

plt.show()
