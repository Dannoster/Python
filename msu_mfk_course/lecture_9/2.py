import pandas as pd
import numpy as np

df = pd.read_csv("input.csv", header=None, names = np.arange(1,11))
df = df.mean().sort_values().index[0]

print(df)