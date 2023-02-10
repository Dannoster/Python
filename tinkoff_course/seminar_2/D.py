m, n = input().split()
m, n = int(m), int(n)

matrix = []
for _ in range(m):
    matrix.append(n*[0])

number = 1
i, j = 0, 0


matrix[i][j] = 1
number += 1
while not matrix[i][j+1] != 0:
    while matrix[i][j+1] == 0:
        matrix[i][j+1] = number
        number += 1
        j += 1
        if j == n - 1:
            break

    while matrix[i+1][j] == 0:
        matrix[i+1][j] = number
        number += 1
        i += 1
        if i == m - 1:
            break

    while matrix[i][j-1] == 0:
        matrix[i][j-1] = number
        number += 1
        j -= 1
        if j == 0:
            break

    while matrix[i-1][j] == 0:
        matrix[i-1][j] = number
        number += 1
        i -= 1
        if i == 0:
            break

for line in matrix:
    print(*line)