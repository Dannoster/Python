import numpy as np
import pandas as pd

df = pd.read_csv("learning/tinkoff/lecture_5/train.csv")

new_df = df.groupby(["SibSp","Parch"]).mean()["Survived"].sort_values(ascending=False).reset_index()

print(new_df)
del df, new_df

