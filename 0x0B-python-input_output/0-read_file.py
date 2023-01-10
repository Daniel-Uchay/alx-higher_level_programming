#!/usr/bin/python3
"""This module contains a function that
reads a text file
"""


def read_file(filename=""):
    """This function reads a file"""
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
