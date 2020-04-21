import csv
import math
import matplotlib.pyplot as plt

f = open("data-hanum.csv")
reader = csv.reader(f)

def f(x):
    return (((9.8*68/x*(1-math.exp(-x/68)**10))-40))

x = [i[1] for i in reader]
y = []

for row in x:
    y.append(f(float(row)))

plt.plot(x, y, "*")
plt.show()
