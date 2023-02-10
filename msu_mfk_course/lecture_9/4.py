import pandas as pd

df = pd.read_csv("input.csv")
df = df.sum().sort_values(ascending=False)

if df.sum() >= 8_000_000:
    print(1, end=" ")
print(df.index[0])