#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = list(set(my_list))
    res = 0
    for x in range(len(unique)):
        res += unique[x]

    return res
