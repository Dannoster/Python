import numpy as np
import pandas as pd

df = pd.read_csv("learning/tinkoff/lecture_5/train.csv")

male_total = df[ df["Sex"] == "male" ]
male_alive = male_total[ male_total["Survived"] == 1 ]

female_total = df[ df["Sex"] == "female" ]
female_alive = female_total[ female_total["Survived"] == 1 ]

del df


print(male_alive.shape[0]/male_total.shape[0], female_alive.shape[0]/female_total.shape[0])