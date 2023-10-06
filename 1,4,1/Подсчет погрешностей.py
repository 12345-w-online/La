import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data_table = pd.read_csv('Новая таблица - Лист1.csv')
data = data_table.to_numpy().flatten()


print(np.unique(data, return_counts=True))