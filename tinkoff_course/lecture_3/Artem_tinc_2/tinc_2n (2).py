# -*- coding: utf-8 -*-
"""tinc_2n.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NK4qmdnG3xHiZEoZRNbNNN5i3XHyKi2l
"""

''' b
str = input()
used_nums = set()
twice_nums = set()
ans = []
for char in str:
    if char.isdigit():
        if char in used_nums:
            twice_nums.add(char)
        used_nums.add(char)

if (len(twice_nums) != 0):
    for value in twice_nums:
        ans.append(value)
    ans.sort()
    print(' '.join(ans))
else:
    print("NO")
    '''

''' f
n = int(input())
languages = {}
for i in range(n):
    langs_amount = int(input())
    for j in range(langs_amount):
        temp_lang = input()
        if temp_lang not in languages:
            languages[temp_lang] = []

        languages[temp_lang].append(i)

everyone = []
for key in languages:
    if len(languages[key]) == n:
        everyone.append(key)
print(len(everyone))

for lang in everyone:
    print(lang)

print(len(languages))
for key in languages:
    print(key)
'''

'''
n = int(input())
states = {}
for i in range(n):
    state, voters = input().split()
    states[state] = int(voters)

c = int(input())
states_votes = {}
presidents = {}
for i in range(c):
    state, vote_for = input().split()
    presidents[vote_for] = 0
    if states_votes.get(state) == None:
        states_votes[state] = []
    states_votes[state].append(vote_for)

for state, voters in states.items():
    max = ['', 0]
    for president in presidents.keys():
        temp = states_votes[state].count(president)
        if temp >= max[1]:
            if temp == max[1] and president < max[0] or temp > max[1]:
                max = [president, temp]
    presidents[max[0]] += voters

ans = []
for president,votes in presidents.items():
    ans.append([votes, president])
ans.sort()
for votes, president in ans:
    print(president, votes, sep=' ')
'''

#2
#Florida 25
#Pennsylvania 23
#11
#Florida Gore
#Pennsylvania Gore
#Florida Bush
#Pennsylvania Gore
#Pennsylvania Bush
#Florida Gore
#Pennsylvania Gore
#Florida Bush
#Pennsylvania Gore
#Florida Bush
#Pennsylvania Gore

def min4(a, b, c, d):
    return min(a,b,c,d)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min(a,b,c,d))

