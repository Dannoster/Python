a = input().split()
for i in range(len(a)): a[i] = int(a[i])

maxim = max(a)
max_index = a.index(maxim)
minim = min(a)
min_index = a.index(minim)

a[max_index] = minim
a[min_index] = maxim
# print(maxim, minim, max_index, min_index)
print(*a, end = " \n")


