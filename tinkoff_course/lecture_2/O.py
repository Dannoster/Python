a = input().split()
max, item = 0, 0
for i, item in enumerate(a):
    if len(item) > max:
        max = len(item)
        number = i
print(a[number])
print(max)
