import numpy as np

table = np.genfromtxt("input.csv", delimiter=",")
table.sum(axis=0)
sums = list(table.sum(axis=0))
print(sums.index(max(sums))+1)