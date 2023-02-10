a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
b = int(input())
for i, height in enumerate(a):
    if height < b:
        print(i+1)
        break
    elif i == len(a)-1:
        print(len(a)+1)
    elif a == []:
        print(1)
