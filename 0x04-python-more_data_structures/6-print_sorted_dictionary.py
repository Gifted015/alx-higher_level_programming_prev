#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = sorted(list(a_dictionary))
    for x in sort:
        print("{}: {}".format(x, a_dictionary[x]))
