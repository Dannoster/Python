import numpy as np
import pandas as pd

df = pd.read_csv("learning/tinkoff/lecture_5/train.csv")

w_sib_ttl = df[ df["SibSp"] != 0 ] # не нужно
w_sib_and_parch_ttl = w_sib_ttl[ w_sib_ttl["Parch"] != 0 ] 
wo_sib_ttl = df[ df["SibSp"] == 0 ]
wo_parch_ttl = df[ df["Parch"] == 0 ]
wo_sib_and_parch_ttl = wo_sib_ttl[ wo_sib_ttl["Parch"] == 0 ] 

w_sib_and_parch_al = w_sib_and_parch_ttl[ w_sib_and_parch_ttl["Survived"] == 1 ]
wo_sib_al = wo_sib_ttl[ wo_sib_ttl["Survived"] == 1 ]
wo_parch_al = wo_parch_ttl[ wo_parch_ttl["Survived"] == 1 ]
wo_sib_and_parch_al = wo_sib_and_parch_ttl[ wo_sib_and_parch_ttl["Survived"] == 1 ]


print(w_sib_and_parch_al.shape[0]/w_sib_and_parch_ttl.shape[0], wo_sib_al.shape[0]/wo_sib_ttl.shape[0], wo_parch_al.shape[0]/wo_parch_ttl.shape[0], wo_sib_and_parch_al.shape[0]/wo_sib_and_parch_ttl.shape[0])
