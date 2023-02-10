import numpy as np

with open("input.txt") as file:
    mas = np.array([float(num) for num in file.read().strip().split()])

print(f"{np.median(mas):.02f} {np.mean(mas):.02f} {np.std(mas):.02f}")