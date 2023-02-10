def rec():
    a = input()
    if a == '0':
        print(a)
        return None
    rec()
    print(a)
rec()

