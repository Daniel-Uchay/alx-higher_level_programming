#!/usr/bin/python3
def best_score(a_dictionary):
    new_dictionary = {}

    aux = 0
    if a_dictionary:
        for key in a_dictionary:
            if a_dictionary[key] > aux:
                new_dictionary['name'] = key
                aux = a_dictionary[key]
        return new_dictionary['name']
    else:
        return None
