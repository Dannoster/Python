import numpy as np

table = np.genfromtxt("input.csv", delimiter=",")
persons_total = len(table)
type_1_persons = sum(table.std(axis=1) <= 4)

pair = type_1_persons, persons_total-type_1_persons
print(pair.index(max(pair)) + 1)