#!/usr/bin/python3
def add_tuple(tuple_a=(0, 0), tuple_b=(0, 0)):
    try:
        a_0 = tuple_a[0]
    except IndexError:
        a_0 = 0
    try:
        b_0 = tuple_b[0]
    except IndexError:
        b_0 = 0
    try:
        a_1 = tuple_a[1]
    except IndexError:
        a_1 = 0
    try:
        b_1 = tuple_b[1]
    except IndexError:
        b_1 = 0

    first = a_0 + b_0
    second = a_1 + b_1
    result = first, second
    return result
