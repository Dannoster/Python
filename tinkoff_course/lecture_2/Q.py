a = input()

left = a.find('h')
right = len(a) - 1 - a[::-1].find('h')

a = a[:left]+a[right+1:]
print(a)


    