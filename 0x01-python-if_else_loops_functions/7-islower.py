#!/usr/bin/python3
def islower(c):
    for x in range(97, 123):
        if c == chr(x):
            return True
    else:
        return False
