a = input().split()
b = int(input())

a.pop(b)
print(*a, end = " \n")