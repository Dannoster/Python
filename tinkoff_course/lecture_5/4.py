import numpy as np
import pandas as pd

df = pd.read_csv("learning/tinkoff/lecture_5/train.csv")

ans = df["Cabin"].dropna().value_counts().shape[0]

print(ans)