import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def to_excel(s):
    return ' '.join([*map(str, list(s))]).split()

data_table = pd.read_csv('Новая таблица - Лист1.csv')
data_20 = data_table.to_numpy().flatten()

values_10 = np.array([i for i in range(4, 26)])
counts_10 = np.array([2, 4, 3, 8, 11, 11, 39, 23, 52,
                      46, 36, 38, 36, 23, 20, 14, 11, 10,
                      5, 2, 5, 1])
data_10 = []
for i in range(len(values_10)):
    data_10 += [values_10[i]] * counts_10[i]
data_10 = np.array(data_10)

hist_10 = pd.DataFrame(np.vstack((values_10, counts_10)))

values_20, counts_20 = np.unique(data_20, return_counts=True)

data_40 = np.empty(100, dtype=int)
# print(data_40)
for i in range(100):
    data_40[i] = data_20[2*i] + data_20[2*i + 1]
values_40, counts_40 = np.unique(data_40, return_counts=True)

hist_10 = pd.DataFrame(np.vstack((values_10, counts_10, to_excel(counts_10/100))))
# print(hist_10)
hist_10.to_csv('Данный для гистограммы 10сек.xlsx')

hist_20 = pd.DataFrame(np.vstack((values_20, counts_20, to_excel(counts_20/100))))
# print(hist_20)
hist_20.to_csv('Данный для гистограммы 20сек.xlsx')

hist_40 = pd.DataFrame(np.vstack((values_40, counts_40, to_excel(counts_40/100))))
# print(hist_40)
hist_40.to_csv('Данный для гистограммы 40сек.xlsx')

fig, ax1 = plt.subplots()
fig.set_figheight(16)
fig.set_figwidth(32)

color = 'tab:red'
# ax1.set_xlabel('$n$  (10с)', fontsize=30, color=color)
ax1.set_ylabel(r'$\omega$', fontsize=30)
ax1.hist(data_10, np.arange(0, 91), alpha=0.5, density=True, label='10с', color=color)

ax1.tick_params(axis='x', labelcolor="black",  labelsize=30)
ax1.tick_params(axis='y', labelcolor='#000000',  labelsize=30)
plt.legend(loc='upper left', fontsize=25)

color = 'tab:green'
ax3 = ax1.twiny()
# ax3.set_xlabel('$n$  (20с)', fontsize=30, color=color)

ax3.hist(data_20, np.arange(0, 91), alpha=0.5, density=True, label='20с', color=color)
ax3.tick_params(axis='x', labelcolor="black", labelsize=25)
fig.tight_layout()
plt.legend(loc='upper center', fontsize=30)

color = 'tab:blue'
ax2 = ax1.twiny()
# ax2.set_xlabel('$n$  (40с)', fontsize=30, color=color)

ax2.hist(data_40, np.arange(0, 91), alpha=0.5, density=True, label='40с', color=color)
ax2.tick_params(axis='x', labelcolor="black", labelsize=25)
fig.tight_layout()
plt.legend(loc='upper right', fontsize=30)

plt.savefig('histogram.png')
plt.show()

print("Среднее значение 10", np.sum(data_10)/400, "σ отдельного", np.std(data_10), "σ среднего", np.std(data_10) / (data_10.size ** (1 / 2)),
      "ε1", np.std(data_10) / (data_10.size ** (1 / 2)) / np.mean(data_10) * 100, "ε2", 100 / ((np.mean(data_10 * data_10.size)) ** (1 / 2)))

print("Среднее значение 20", np.sum(data_20)/200, "σ отдельного", np.std(data_20), "σ среднего", np.std(data_20) / (data_20.size ** (1 / 2)),
      "ε1", np.std(data_20) / (data_20.size ** (1 / 2)) / np.mean(data_20) * 100, "ε2", 100 / ((np.mean(data_20 * data_20.size)) ** (1 / 2)))

print("Среднее значение 40", np.sum(data_40)/100, "σ отдельного", np.std(data_40), "σ среднего", np.std(data_40) / (data_40.size ** (1 / 2)),
      "ε1", np.std(data_40) / (data_40.size ** (1 / 2)) / np.mean(data_40) * 100, "ε2", 100 / ((np.mean(data_40 * data_40.size)) ** (1 / 2)))



# data_40_trans = np.abs(data_40 - np.mean(data_40))
# data_10_trans = np.abs(data_10 - np.mean(data_10))
#
# np.sum(data_10_trans < np.std(data_10)), np.sum(data_10_trans < 2*np.std(data_10))
#
# np.sum(data_40_trans < np.std(data_40)), np.sum(data_40_trans < 2*np.std(data_40))
#
# np.sum(data_10_trans > 2 * np.std(data_10))