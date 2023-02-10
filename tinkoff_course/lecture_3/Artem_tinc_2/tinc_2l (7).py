# -*- coding: utf-8 -*-
"""tinc_2l.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NK4qmdnG3xHiZEoZRNbNNN5i3XHyKi2l
"""

def Rule(a):
    return -a[1], a[0]

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
    if vote_for not in presidents:
        presidents[vote_for] = 0
    if state not in states_votes:
        states_votes[state] = []
    states_votes[state].append(vote_for)

for state, voters in states.items():
    presidents_in_state = {}
    for vote_for in states_votes[state]:
        if vote_for not in presidents_in_state:
            presidents_in_state[vote_for] = 0
        presidents_in_state[vote_for] += 1
    max = ["", 0]
    for president, votes in presidents_in_state.items():
        if votes >= max[1]:
            if votes > max[1] or president < max[0]:
                max = [president, votes]
    presidents[max[0]] += voters

del states
del states_votes

for president, votes in sorted(presidents.items(), key = Rule):
    print(president, votes, sep=' ')


