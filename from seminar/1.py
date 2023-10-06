from statistics import mean
import matplotlib.pyplot as plt

with open('output.txt', 'r') as fin:
	data = fin.readlines()

current = [float(line.split()[0]) for line in data[1:]]
voltage = [float(line.split()[1]) for line in data[1:]]

def l_s(xdata, ydata):
	a = (sum([x * y for x, y in zip(xdata, ydata)]) - mean(ydata) * sum(xdata)) / (sum([x**2 for x in xdata]) - mean(xdata) * sum(xdata))
	b = mean(ydata) - a * mean(xdata)
	return a, b

print(l_s(current, voltage))
a, b = l_s(current, voltage)

fig, ax = plt.subplots()
ax.plot(current, voltage, 'o', label = 'exp data')

xdata = list(range(21))
ax.plot(xdata, [a*x+b for x in xdata], label = 'approx')
ax.set_xlabel('current, A')
ax.set_ylabel('voltage, V')
ax.legend()
plt.savefig('fig1.png')
plt.show()
