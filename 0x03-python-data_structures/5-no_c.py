#!/usr/bin/python3
def no_c(my_string):
    copy_string = my_string.translate({ord(letter): None for letter in 'cC'})
    return copy_string
