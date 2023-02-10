import numpy as np

stds =[]
with open("input.csv") as file:
    lines = file.readlines()
    
total = len(lines)
count_1 = 0
for line in lines:
    line = line.split(",")
    line = [int(numb) for numb in line]
    if np.std(line) <= 4:
        count_1 += 1

pair = (count_1, total - count_1)

print(pair.index(max(pair)) + 1)
