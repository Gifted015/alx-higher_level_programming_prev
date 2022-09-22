#!/usr/bin/python3
def uppercase(c):
    i = 0
    while i < len(c):
        a = ord(c[i])
        if a >= 97 and a < 123:
            a = a - 32
        print("{}".format(chr(a)), end="")
        i += 1
    print("")
