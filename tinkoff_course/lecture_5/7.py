import numpy as np
import pandas as pd

df = pd.read_csv("learning/tinkoff/lecture_5/train.csv")

ans = np.array(df["Name"])
ans = np.quantile([len(item.split()) for item in ans], 0.95)

del df

print(ans)