animals = dict()

with open("input.txt") as file:
    for line in file:
        splitted_line = line.split()
        animal = splitted_line[1]
        gender = splitted_line[2]
        if animal not in animals:
            animals[animal] = set()
        animals[animal].add(gender)

result = tuple(filter(lambda animal: len(animals[animal]) == 2, animals))
if result:
    print(*sorted(result, key=lambda name: len(name)), sep="\n")
else:
    print(0)