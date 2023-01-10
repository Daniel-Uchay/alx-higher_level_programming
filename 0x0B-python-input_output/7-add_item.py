#!/usr/bin/python3
"""This script that adds all arguments
to a Python list, and then save them to a file
"""


import sys
from os import path
"""Import the json module and sys module"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""Import the save to json file function"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""Import the save to json file function"""

ret_list = []

if path.isfile("add_item.json") is False:
    save_to_json_file(ret_list, "add_item.json")

ret_list = load_from_json_file("add_item.json")

if sys.argv[1:]:
    for i in sys.argv[1:]:
        ret_list.append(i)

save_to_json_file(ret_list, "add_item.json")
