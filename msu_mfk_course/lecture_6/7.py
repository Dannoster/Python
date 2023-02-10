animals = dict()

with open("input.txt") as file:
    for line in file:
        splitted_line = line.split()
        id_ = splitted_line[0]        
        animal = splitted_line[1]
        if animal not in animals:
            animals[animal] = list()
        animals[animal].append(id_)

sorted_animals = sorted(animals, key=lambda name: len(name))
for animal in sorted_animals:
    ids = animals[animal]
    print(f"{animal}: ", end='')
    print(*sorted(ids), sep=", ")