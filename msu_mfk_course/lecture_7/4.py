import numpy as np

with open("input.txt") as file:
    first_day_prod = int(file.readline().strip())
    last_day_prod = int(file.readline().strip())
    days = int(file.readline().strip())

# step = (last_day_prod - first_day_prod) / (days - 1)
# estim_arr = np.linspace(first_day_prod, last_day_prod, days)
fact_arr = np.linspace(first_day_prod, last_day_prod, days)

for i in range(0, len(fact_arr), 7):
    fact_arr[i] = fact_arr[i]/3

for i in range(4, len(fact_arr), 7):
    fact_arr[i] = 2*fact_arr[i]

with open("output.txt", "w") as file:
    for prod in fact_arr:
        file.write(f"{prod:.02f}\n")
    

# print(*zip(estim_arr,fact_arr))