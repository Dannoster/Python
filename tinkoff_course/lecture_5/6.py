import numpy as np
import pandas as pd

df = pd.read_csv("learning/tinkoff/lecture_5/train.csv")

med_age = df["Age"].median()
new_df = df["Age"].fillna(med_age)
average = new_df.mean()

del df

print(average)