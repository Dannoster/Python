import numpy as np

table = np.genfromtxt("input.csv", delimiter=",")

table[0] = 1.5 * table.mean(axis=0)

np.savetxt("output.csv", table, fmt="%i", delimiter=",")