#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list != None:
        for x in range(len(my_list) - 1, -1, -1):
            if type(my_list[x]) == int:
                print("{:d}".format(my_list[x]))
