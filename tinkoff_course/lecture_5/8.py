import numpy as np
import pandas as pd

df = pd.read_csv("learning/tinkoff/lecture_5/train.csv")

ans = np.array(df["Name"])
line: str = ""
shorts = []
for line in ans:
    dot_index = line.find(".")
    short = line[ :dot_index].split()[-1]
    shorts.append(short)

del df

new_df = pd.DataFrame(shorts).value_counts().head()

print(new_df)