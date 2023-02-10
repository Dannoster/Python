import numpy as np
import pandas as pd

df = pd.read_csv("learning/tinkoff/lecture_5/train.csv")

without_sib_total = df[ df["SibSp"] == 0 ]
without_sib_alive = without_sib_total[ without_sib_total["Survived"] == 1 ]

without_parch_total = df[ df["Parch"] == 0 ]
without_parch_alive = without_sib_total[ without_sib_total["Survived"] == 1 ]

del df

# print(without_sib_total, without_sib_alive, without_parch_total, without_parch_alive)
print(without_sib_alive.shape[0]/without_sib_total.shape[0], without_parch_alive.shape[0]/without_parch_total.shape[0])