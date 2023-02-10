m, n = input().split()
m, n = int(m), int(n)

matrix = []
for _ in range(m):
    matrix.append(n*[0])

i, j = 0, 0
number = 1
direction = {"down" : (1, 0), "upright" : (-1, 1), "right" : (0, 1), "downleft" : (1, -1)}

while i < m and j < n:
    matrix[i][j] = number
    if i == m - 1 and j == n - 1:
        break
    if i < m - 1:
        delta_i, delta_j = direction["down"]
    elif i == m-1:
        delta_i, delta_j = direction["right"]
    i += delta_i
    j += delta_j
    number += 1

    while i > 0:
        if j == n - 1:
            break
        matrix[i][j] = number
        delta_i, delta_j = direction["upright"]
        i += delta_i
        j += delta_j
        number += 1

    matrix[i][j] = number
    if i == m - 1 and j == n - 1:
        break
    elif j < n - 1:
        delta_i, delta_j = direction["right"]
    else:
        delta_i, delta_j = direction["down"]
    i += delta_i
    j += delta_j
    number += 1

    while j > 0:
        if i == m - 1:
            break
        matrix[i][j] = number
        delta_i, delta_j = direction["downleft"]
        i += delta_i
        j += delta_j
        number += 1

for line in matrix:
    print(*line)