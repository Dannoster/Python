with open("poe_unpublished.txt") as file:
    lines = [   
                        " ".join(sorted(line.split(), key=lambda word: len(word)))
                        for line in file
                    ]
lines = [line+"\n" for line in sorted(lines, key=lambda line: len(line.split()))]
lines[-1] = lines[-1].strip()

with open("poe_decode_attempt.txt", "w") as file:
    file.writelines(lines)