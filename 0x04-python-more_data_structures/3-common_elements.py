#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set()
    for i in set_1:
        if i in set_2:
            new_set.add(i)
    return new_set
