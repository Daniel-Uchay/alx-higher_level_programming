#!/usr/bin/python3
"""This module contains a function called from_json_string"""

import json


def from_json_string(my_str):
    """from_json_string function that transform json my_str to python
    Args:
        my_str (json string): is a JSON string
    """
    return json.loads(my_str)
