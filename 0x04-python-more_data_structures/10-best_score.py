#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    key_list = list(a_dictionary)
    biggest = 0
    for x in range(len(key_list)):
        curr_key = key_list[x]
        if a_dictionary[curr_key] > biggest:
            biggest = a_dictionary[curr_key]
            key = curr_key
    return key
