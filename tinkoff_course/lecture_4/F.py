class Graph:


    def __init__(self, file_name="input.txt"):
        self.adjacency_list = []
        with open(file_name) as file:
            for line in file:
                self.adjacency_list.append(line.strip().split())
        self.adjacency_list.pop(0) # N не нужно
        self.__generate_matrix()

    def __generate_matrix(self):
        size = len(self.adjacency_list)
        self.matrix = [[0 for _ in range(size)] for __ in range(size)]
        for i, line in enumerate(self.adjacency_list):
            for j in line:
                if j != "0":
                    self.matrix[i][int(j)-1] = 1

    def save_matrix(self, file_name="output.txt"):
        with open(file_name, "w") as file:
            for line in self.matrix:
                for numb in line:
                    file.write(f"{numb} ")
                file.write("\n")

a = Graph()
a.save_matrix()


