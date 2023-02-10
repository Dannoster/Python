with open("weights.txt") as file:
    lines = [line.strip()+"\n" for line in file]
lines.sort(key=lambda line: float(line.split()[1]), reverse=True)

lines1 = [pair[1] for pair in enumerate(lines) if pair[0]%2 == 0]
lines2 = [pair[1] for pair in enumerate(lines) if pair[0]%2 == 1]
lines2[-1] = lines2[-1].strip()

with open("team.txt", "w") as ans_file:
    ans_file.writelines(lines1+lines2)