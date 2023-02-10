str1 = input()
str2 = input()
new_str = ""
for code in range(ord("a"), ord("z") + 1):
    letter = chr(code)
    if letter not in str1.lower() and letter not in str2.lower():
        new_str += letter
if new_str:
    print(new_str.upper())
else:
    print(0)