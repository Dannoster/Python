import pandas as pd
import numpy as np

df = pd.read_csv("input.csv")

df.dropna(subset=["name"], inplace=True)
df.fillna(df["score"].mean(), inplace=True)

# print(df)

df.to_csv("output.csv")