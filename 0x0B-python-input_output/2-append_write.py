#!/usr/bin/python3
"""This module contains a function that
appenda string to a text file
"""


def append_write(filename="", text=""):
    """This function append a string to a file"""
    with open(filename, mode="a", encoding="utf-8") as file:
        ret = file.write(text)

    return ret
