#!/usr/bin/python3
"""This module contains a function that
write a text file
"""


def write_file(filename="", text=""):
    """This function write a file"""
    with open(filename, mode="w", encoding="utf-8") as file:
        ret = file.write(text)

    return ret
