n = int(input())
countryOf = {}
for i in range(n):
    line = input().split()
    country = line[0]
    cities = line[1:]
    for city in cities:
        countryOf[city] = country

cities = []
m = int(input())
for i in range(m):
    cities.append(input())
for city in cities:    
    print(countryOf[city])