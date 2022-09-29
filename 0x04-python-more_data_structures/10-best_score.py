#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(list(a_dictionary)) == 0:
        return None
    biggest = 0
    for curr_key in a_dictionary.keys():
        if a_dictionary[curr_key] is None:
            return None
        if a_dictionary[curr_key] > biggest:
            biggest = a_dictionary[curr_key]
            key = curr_key
    return key
