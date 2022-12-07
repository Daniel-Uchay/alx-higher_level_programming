#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        r_s = roman_string
        numero = 0
        for lx in range(len(r_s)):
            if lx > 0 and (rom[r_s[lx]] > rom[r_s[lx - 1]]):
                numero += rom[r_s[lx]] - (2 * rom[roman_string[lx - 1]])
            else:
                numero += rom[r_s[lx]]
        return numero
    return (0)
