import itertools

f = open('studygroup.txt', 'r')
names = f.readline().split()
f.close()

for three_names in itertools.combinations(names, 3):
    print(f"1: {three_names[0]} 2: {three_names[1]} 3: {three_names[2]}")