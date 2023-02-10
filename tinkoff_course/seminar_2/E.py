import numpy as np
 
N = int(input())
magic_square = np.zeros((N,N), dtype=int)
 
n = 1
i, j = 0, N//2
 
while n <= N**2:
    magic_square[i, j] = n
    n += 1
    newi, newj = (i-1) % N, (j+1)% N
    if magic_square[newi, newj]:
        i += 1
        i %= N
    else:
        i, j = newi, newj
    # for line in magic_square:   print(*line)
    # print()

for line in magic_square:
    print(*line)