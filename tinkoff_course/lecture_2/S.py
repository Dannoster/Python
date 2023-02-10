a = input()
new = ""
for i in range(len(a)):
    if i % 3 != 0:
        new += a[i]
print(new)