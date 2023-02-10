


from math import sqrt


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

print(f'{distance(x1, y1, x2, y2):.5f}')