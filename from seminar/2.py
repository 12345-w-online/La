import random
import numpy as np

n = int(input())
a, b = map(int, input().split())

start = 2
finish = 200
sigma_b = 2
x = [i + random.gauss(0.0, (finish - start) / (2 * n)) for i in np.linspace(start, finish, n)]
y = [(j * a) + b + random.gauss(0.0, (((finish - start) / (2 * n)) ** 2 + sigma_b ** 2) ** (1/2)) for j in x]

with open('output.txt', 'w') as f:
    f.write('x y\n')
    for i in range(len(x)):
        f.write(f'{x[i]} {y[i]}\n')
