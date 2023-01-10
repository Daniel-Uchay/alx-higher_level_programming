#!/usr/bin/python3
"""This module contains a function that
serialize a object into Json
"""


import json
"""Import the json module"""


def to_json_string(my_obj):
    """This function serialize an object"""
    return json.dumps(my_obj)
