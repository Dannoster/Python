n = 55
while not (1e-12 + pow(10, -n) != 1e-12 and 1e-12 + pow(10, -(n + 1)) == 1e-12):
    print(pow(10, -n))
    n -= 1
print(n)