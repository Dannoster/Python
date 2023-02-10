import numpy as np
import pandas as pd

df = pd.read_csv("learning/tinkoff/lecture_5/train.csv")

ans = df["Fare"].quantile(3/4)

print(ans)