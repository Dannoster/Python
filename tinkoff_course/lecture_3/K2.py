n = int(input())
parentOf = dict()
setOfAll = set()
numberOfChildrenOf = dict()

for i in range(n-1):
    child, parent = input().split()
    if numberOfChildrenOf.get(parent) != None:
        numberOfChildrenOf[parent] += 1
    else:
        numberOfChildrenOf[parent] = 1

    if numberOfChildrenOf.get(child) == None:
        numberOfChildrenOf[child] = 0

    parentOf[child] = parent
    currentParent = parent
    while parentOf.get(currentParent) != None:
        numberOfChildrenOf[parentOf[currentParent]] += 1
        currentParent = parentOf[currentParent]

for parent in sorted(numberOfChildrenOf):
    print(parent, numberOfChildrenOf[parent])
