class Fort:


    def __init__(self, file_name):
        self.values = []
        self.error = False
        self.file_name = file_name
        with open(file_name) as file:
            lines = file.read().split('\n')
            for line in lines:
                try:
                    if line.isdigit():
                        self.__add(line)
                    elif line == "DROP":
                        self.__drop_num()
                    elif line == "SWAP":
                        self.__swap()
                    elif line == 'DUP':
                        self.__duplicate()
                    elif line == 'OVER':
                        self.__over()
                    elif line in "+-*/":
                        self.do_math(line)
                    elif line == '':
                        break
                    else:
                        self.error = True
                except:
                    self.error = True

    def __del__(self):
        self.write()
    
    def __add(self, value):
        self.values.append(value)

    def __drop_num(self):
        self.values.pop()

    def __swap(self):
        temp = self.values[-1]
        self.values[-1] = self.values[-2]
        self.values[-2] = temp
    
    def __duplicate(self):
        self.values.append(self.values[-1])

    def __over(self):
        self.values.append(self.values[-2])

    def __do_math(self, type):
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

    def write(self, file_name="output.txt"):
        with open(file_name, "w") as file:
            if self.error:
                file.write("ERROR")
            elif not self.values:
                file.write("EMPTY")
            else:
                file.write(' '.join(self.values))
            del self.values


a = Fort("input.txt")
del a