#!/usr/bin/python3
def islower(c):
    c = ord(c)
    for x in range(97, 123):
        if c == x:
            return True
    else:
        return False
