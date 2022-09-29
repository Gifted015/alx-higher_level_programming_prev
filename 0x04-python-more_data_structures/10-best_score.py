#!/usr/bin/python3
def best_score(a_dictionary):
    try:
        key_list = list(a_dictionary)
    except TypeError:
        return None

    x = 0
    for x in range(len(key_list) - 1):
        next_key = key_list[x + 1]
        curr_key = key_list[x]
        if a_dictionary[curr_key] > a_dictionary[next_key]:
            biggest = curr_key

    if x == 0:
        return None

    return biggest
