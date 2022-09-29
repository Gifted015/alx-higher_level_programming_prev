#!/usr/bin/python3
def best_score(a_dictionary):
    key_list = list(a_dictionary)

    for x in range(1, len(key_list)):
        prev_key = key_list[x - 1]
        curr_key = key_list[x]
        biggest = prev_key

        if a_dictionary[curr_key] > a_dictionary[prev_key]:
            biggest = curr_key

    return biggest
