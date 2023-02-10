import pandas as pd

df = pd.read_csv("input.csv")

is_triangle = (df.a < df.b + df.c) & (df.b < df.c + df.a) & (df.c < df.a + df.b)

print(len(df[is_triangle]))