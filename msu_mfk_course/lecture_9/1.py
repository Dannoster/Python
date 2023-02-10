for x1 in False, True:
    for x2 in False, True:
        for x3 in False, True:
            res = (not x1 and x2 and not x3) or (not x1 and x2 and x3) or (x1 and not x2 and not x3)
            if res == True:
                print(x1, x2, x3)