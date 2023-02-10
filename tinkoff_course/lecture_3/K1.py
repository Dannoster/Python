n = int(input())
childrenOf = dict()
setOfAll = set()

for i in range(n-1):
    child, parent = input().split()
    if childrenOf.get(parent) == None:
        childrenOf[parent] = list()
    childrenOf[parent].append(child) 
    setOfAll.add(child)
    setOfAll.add(parent)
setOfAll = sorted(setOfAll)

# print(childrenOf)

def countChildren(person):
    if childrenOf.get(person) == None:
        return 0
    total = 0
    for child in childrenOf[person]:
        total += countChildren(child)
    return total + len(childrenOf[person])

for person in setOfAll:
    print(person, countChildren(person))
