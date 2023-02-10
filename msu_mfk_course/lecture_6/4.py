from collections import Counter

a = input()

b = Counter(a).most_common()[0][0]

print(b)