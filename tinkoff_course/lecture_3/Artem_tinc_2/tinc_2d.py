# -*- coding: utf-8 -*-
"""tinc_2d.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NK4qmdnG3xHiZEoZRNbNNN5i3XHyKi2l
"""

str = input()
used_nums = set()
twice_nums = set()
ans = []
for char in str:
    if char.isdigit():
        if int(char) in used_nums and int(char) not in twice_nums:
            twice_nums.add(int(char))
            ans.append(char)
        else:
            used_nums.add(int(char))

if len(twice_nums) == 0:
    print("NO", end = '')
else:
    ans.sort()
    print(' '.join(ans))
