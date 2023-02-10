signs = ".,;:!?"
sum = 0
str = input()
for item in str:
    if item in signs:
        sum += 1
print(sum)