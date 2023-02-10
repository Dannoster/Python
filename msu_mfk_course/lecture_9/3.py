import pandas as pd
# import numpy as np

df = pd.read_csv("input.csv")
print(df.mean().sort_values(ascending=False).index[0])