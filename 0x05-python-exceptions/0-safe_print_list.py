#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    for y in range(0, x):
        try:
            print(my_list[y])
            length += 1
        except:
            break
    return length
