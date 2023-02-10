animals = set()

with open("input.txt") as file:
    for line in file:
        animals.add(line.split()[1])

print(*sorted(animals, key=lambda name: len(name)), sep="\n")