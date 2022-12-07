#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list:
        w_a = 0.0
        divs = 0
        divd = 0
        for i in my_list:
            divd += i[0] * i[1]
            divs += i[1]
        w_a = divd / divs
        return w_a
    return (0)
