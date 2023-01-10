#!/usr/bin/python3
"""This module contain a function that
returns a list of lists of integers representing
the Pascal's triangle of n"""


def pascal_triangle(n):
    """ Arguments:
            n - make a pascal triangle of n
        Return: The pascal triangle
    """
    lis = []

    if n <= 0:
        return lis

    for i in range(n):
        lis.append([])
        lis[i].append(1)
        for m in range(1, i):
            lis[i].append(lis[i - 1][m - 1] + lis[i - 1][m])
        if n != 0 and i != 0:
            lis[i].append(1)

    return lis
