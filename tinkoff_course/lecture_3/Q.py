n = int(input())

def phib(n):
    if n == 1 or n == 2:
        return 1
    return phib(n-1) + phib(n-2)

print(phib(n))