class Mechanism():
    def __init__(self):
        self.commands = {}
        self.journal = []
        self.day = 0

    def add_command(self, line):
        self.commands[line[0]] = int(line[1])

    def read_command(self, line):
        hours, minutes = line[0].split(':')
        time = int(hours)*60 + int(minutes) + self.day*24*60
        if line[1] == 'DEL':
            self.delete(time)
        else:
            if self.journal:
                if time < self.journal[-1][-1]:
                    self.day += 1
                    time = int(hours)*60 + int(minutes) + self.day*24*60
                beg_time = max(self.journal[-1][2] , time)
            else:
                beg_time = time
            self.journal.append([line[1], beg_time, beg_time + self.commands[line[1]], time])

    def delete(self, time):
        if self.journal[-1][1] > time:
            self.journal.pop()

    def to_file(self, filename):
        with open(filename, 'w') as file:
            for line in self.journal:
                file.write(self.convert_time(line[1]) + ' ' + str(line[0]) + '\n')
            file.write(self.convert_time(self.journal[-1][2]))

    def convert_time(self, min):
        hour = min // 60 % 24
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