a = int(input())

n_minus_2 = 1
n_minus_1 = 0
n = 0

for i in range(a):
    n = n_minus_1 + n_minus_2
    
    n_minus_2 = n_minus_1
    n_minus_1 = n

print(n)
