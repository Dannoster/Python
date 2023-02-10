a = float(input())
n = int(input())

def power(a, n):
    if n == 0:
        return 1
    elif n > 0:
        res = a
        for i in range(n-1):
            res *= a
        return res
    else:
        res = 1/a
        for i in range(-n-1):
            res /= a
        return res

print(f"{power(a, n)}")