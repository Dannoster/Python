from math import sin, exp

def f(day):
    return exp(sin(day/100) * day/10) * 20

print(f(18))