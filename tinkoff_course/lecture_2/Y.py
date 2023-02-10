a = input().split()
k, c = input().split()

a.insert(int(k), c)
print(*a, end = " \n")