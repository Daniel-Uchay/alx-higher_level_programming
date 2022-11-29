#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        print(f"{number % 10}", end="")
        return number % 10
    else:
        print(f"{(number * -1) % 10}", end="")
        return (number * -1) % 10
