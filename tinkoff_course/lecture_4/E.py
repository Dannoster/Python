class Graph():
    
    
    def __init__(self, file_name=None):
        self.matrix = []
        if file_name:
            with open(file_name) as file:
                n = int(file.readline().strip())
                matrix = []
                current_line = []
                for _ in range(n):
                    current_line = [int(numb) for numb in file.readline().strip().split()]
                    matrix.append(current_line)
                    current_line = []
            self.matrix = matrix

    def save_adjacency_lists(self, file_name):
        with open(file_name, "w") as file:
            for line in self.matrix:
                if sum(line) == 0:
                    file.write("0")
                else:
                    for i, number in enumerate(line):
                        if number == 1:
                            file.write(f"{i+1} ")
                file.write("\n")


a = Graph("input.txt")
a.save_adjacency_lists("output.txt")
