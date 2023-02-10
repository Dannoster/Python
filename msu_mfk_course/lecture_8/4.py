import numpy as np

table = np.genfromtxt("input.csv", delimiter=",")

# print(table)
for i, line in enumerate(table):
    for j, numb in enumerate(line):
        if (i+j)%2 == 1:
            # print(f"{numb/2:f}")
            table[i, j] = numb/2 

# print(table)
np.savetxt("output.csv", table, delimiter=",", fmt='%g')
