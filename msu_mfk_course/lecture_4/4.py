with open("the_calls.txt") as file:
    calls = [line.split() for line in file]

calls.sort(key=lambda call: float(call[1]), reverse=True)

calls_A = ['\t'.join(call)+'\n' for call in calls if call[2] == 'A']
calls_B = ['\t'.join(call)+'\n' for call in calls if call[2] == 'B']
calls_B[-1] = calls_B[-1].strip()

with open("calls.txt", "w") as file:
    file.writelines(calls_A+calls_B)