#!/usr/bin/python3
def remove_char_at(str, n):

    if len(str) > n and n >= 0:
        strCopy = str.replace(str[n], '')
        return strCopy
    else:
        return str
