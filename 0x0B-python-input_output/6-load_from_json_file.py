#!/usr/bin/python3
"""This module contains a function that
creates an Object from a “JSON file”
"""


import json
"""Import the json module"""


def load_from_json_file(filename):
    """ Arguments:
        filename - file to extract the json string
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
