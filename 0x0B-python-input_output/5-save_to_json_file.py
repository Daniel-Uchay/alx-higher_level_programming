#!/usr/bin/python3
"""This module contains a function that
writes an Object to a text file, using a JSON
representation
"""


import json
"""Import the json module"""


def save_to_json_file(my_obj, filename):
    """ Arguments:
            my_obj - object to encode to JSON string
            filename - file where json string have to be
            stored
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
