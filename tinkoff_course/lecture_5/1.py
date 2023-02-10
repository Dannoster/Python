import pandas as pd
import numpy as np

df = pd.read_csv('learning/tinkoff/lecture_5/train.csv')
alive = np.where(df["Survived"] == 1)[0]
dead = np.where(df["Survived"] == 0)[0]
print(len(alive), len(dead))
