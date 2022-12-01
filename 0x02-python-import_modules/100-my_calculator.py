#!/usr/bin/python3
if __name__ == "__main__":
    # IMPORTS
    from calculator_1 import add, sub, mul, div
    from sys import argv

    # CONDITIONALS
    if len(argv) != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] != '+' and argv[2] != '-' and argv[2] != '*' and argv[2] != '/':
        print(f"Unknown operator. Available operators: +, -, * and /")
        exit(1)

    # VARIABLES
    a = argv[1]
    b = argv[3]

    # CODE
    if argv[2] == '+':
        print(f"{a} + {b} = {add(int(a), int(b))}")
    if argv[2] == '-':
        print(f"{a} - {b} = {sub(int(a), int(b))}")
    if argv[2] == '*':
        print(f"{a} * {b} = {mul(int(a), int(b))}")
    if argv[2] == '/':
        print(f"{a} / {b} = {div(int(a), int(b))}")
