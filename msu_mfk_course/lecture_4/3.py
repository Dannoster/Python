with open("med_research.txt") as file:
    lines = file.readlines()

m = len(lines)
n = len(lines[0].split())

lines = [line.split() for line in lines]
print(lines)

with open("output.txt", "w") as file:
    for i in range(n):
        for j in range(m):
            file.write(f"{lines[j][i]}")
            if j < m-1: file.write(" ")
        if i < n-1: file.write("\n")