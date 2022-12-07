#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dict_copy = a_dictionary.copy()

    for i, k in dict_copy.items():
        if k == value:
            del a_dictionary[i]

    return a_dictionary
