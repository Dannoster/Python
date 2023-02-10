# -*- coding: utf-8 -*-
"""tinc_oop_b.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NK4qmdnG3xHiZEoZRNbNNN5i3XHyKi2l
"""

class Stack():
    def __init__(self, link):
        self.values = []
        self.error = False
        self.file = link
    
    def add_num(self, value):
        self.values.append(value)

    def drop_num(self):
        self.values.pop()

    def swap_nums(self):
        temp = self.values[-1]
        self.values[-1] = self.values[-2]
        self.values[-2] = temp
    
    def dublicate(self):
        self.values.append(self.values[-1])

    def over(self):
        self.values.append(self.values[-2])

    def mathematic(self, type):
        num_2 = int(self.values.pop())
        num_1 = int(self.values.pop())
        if type == '+':
            self.__add(num_1, num_2)
        elif type == '-':
            self.__minus(num_1, num_2)
        elif type == '*':
            self.__mul(num_1, num_2)
        elif type == '/':
            self.__div(num_1, num_2)

    def __add(self, num_1, num_2):
        self.values.append(str(num_1 + num_2))
    
    def __minus(self, num_1, num_2):
        self.values.append(str(num_1 - num_2))

    def __mul(self, num_1, num_2):
        self.values.append(str(num_1 * num_2))

    def __div(self, num_1, num_2):
        self.values.append(str(num_1 // num_2))

    def read_command(self, line):
        try:
            if line.isdigit():
                self.add_num(line)
            elif line == "DROP":
                self.drop_num()
            elif line == "SWAP":
                self.swap_nums()
            elif line == 'DUP':
                self.dublicate()
            elif line == 'OVER':
                self.over()
            elif line in ['+', '-', '*', '/']:
                self.mathematic(line)
            elif line == '':
                self.__del__()
            else:
                self.error = True
        except:
            self.error = True

    def __del__(self):
        with open(self.file, 'w') as file:
            if self.error:
                file.write("ERROR")
            elif not self.values:
                file.write("EMPTY")
            else:
                file.write(' '.join(self.values))
            del self.values

stack = Stack('output.txt')
with open('input.txt', 'r') as file:
    lines = file.read().split('\n')
    for line in lines:
        stack.read_command(line.strip())

''' Task D
class Mechanism():
    def __init__(self):
        self.commands = {}
        self.journal = []

    def add_command(self, line):
        self.commands[line[0]] = int(line[1])

    def read_command(self, line):
        hours, minutes = line[0].split(':')
        time = int(hours)*60 + int(minutes)
        if line[1] == 'DEL':
            self.delete(time)
        else:
            if self.journal:
                beg_time = max(self.journal[-1][2] , time)
            else:
                beg_time = time
            self.journal.append([line[1], beg_time, beg_time + self.commands[line[1]]])

    def delete(self, time):
        if self.journal[-1][1] > time:
            self.journal.pop()

    def to_file(self, filename):
        with open(filename, 'w') as file:
            for line in self.journal:
                file.write(self.convert_time(line[1]) + ' ' + str(line[0]) + '\n')
            file.write(self.convert_time(self.journal[-1][2]))

    def convert_time(self, min):
        hour = min // 60
        min = min % 60
        return "%02d:%02d" % (hour, min)

mech = Mechanism()
with open('input.txt', 'r') as file:
    lines = file.read().split('\n')
    n = int(lines[0].strip())
    for line in lines[1:n+1]:
        mech.add_command(line.split(' '))
    for line in lines[n+1:]:
        mech.read_command(line.split())

mech.to_file('output.txt')
'''

''' Task f
class Graph():
    def __init__(self, size):
        self.adjacency_list = []
        self.adjacency_matrix = [[0 for _ in range(size)] for __ in range(size)]

    def read_list(self, line):
        self.adjacency_list.append([int(i) for i in line.split()])

    def __build_adjacency_matrix(self):
        for i in range(len(self.adjacency_list)):
            for way in self.adjacency_list[i]:
                if way == 0:
                    continue
                self.adjacency_matrix[i][way - 1] = 1

    def print_matrix(self):
        self.__build_adjacency_matrix()
        for line in self.adjacency_matrix:
            for col in line:
                print(col, end= ' ')
            print()

n = int(input())
graph = Graph(n)
for i in range(n):
    line = input()
    graph.read_list(line)

graph.print_matrix()
'''
