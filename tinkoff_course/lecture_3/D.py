str1 = input()
str2 = input()

common_letters = ""
for letter in str1:
    if letter in str2 and letter not in common_letters:
        common_letters += letter
if common_letters:
    print(*sorted(common_letters), sep = '')
else:
    print("NO")


# new_str = ""
# for code in range(ord("a"), ord("z") + 1):
#     letter = chr(code)
#     if letter not in str1.lower() and letter not in str2.lower():
#         new_str += letter
# if new_str:
#     print(new_str.upper())
# else:
#     print(0)