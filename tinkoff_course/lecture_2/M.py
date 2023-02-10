str = input()
#str = "Abrakadabra"

print(
    str[2],
    str[-2],
    str[:5],
    str[:-2],
    str[::2],
    str[1::2],
    str[::-1],
    str[::-1][::2],
    len(str),
    sep="\n",
    end=''
    )
