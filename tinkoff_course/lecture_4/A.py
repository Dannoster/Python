class Clst:

    def __init__(self, file_name):
        with open(file_name) as file:
            n, l = (int(numb) for numb in file.readline().strip().split())
            numbers = sorted([int(numb) for numb in file.readline().strip().split()])
            clusters = []
            prev_number = numbers.pop(0)
            current_cluster = [prev_number]
            for number in numbers:
                if abs(number - prev_number) <= l:
                    current_cluster.append(number)
                else:
                    clusters.append(current_cluster)
                    current_cluster = [number]
                prev_number = number
            clusters.append(current_cluster)
            self.clusters = clusters

    def file_write(self, file_name):
        with open(file_name, "w") as file:
            total_clusters = len(self.clusters)
            file.write(f"{total_clusters}\n")
            for cluster in self.clusters:
                cluster = [str(numb) for numb in cluster]
                file.write(f'{" ".join(cluster)}\n')


clusters = Clst("input.txt")
clusters.file_write("output.txt")