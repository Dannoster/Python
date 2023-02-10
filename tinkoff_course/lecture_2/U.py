a = input().split()
for i in range(len(a)): a[i] = int(a[i])
print(max(a),a.index(max(a)), end = "")

