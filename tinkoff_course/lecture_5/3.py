import pandas as pd
import numpy as np

df = pd.read_csv('learning/tinkoff/lecture_5/train.csv')

without_port = df[ df["Embarked"].isnull() ].shape[0]

print(without_port)
