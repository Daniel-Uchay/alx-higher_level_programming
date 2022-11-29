#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10

if number >= 0:
    print(f"Last digit of {number} is {lastDigit}", end=" ")

    if lastDigit > 5:
        print(f"and is greater than 5")
    elif lastDigit == 0:
        print(f"and is 0")
    elif lastDigit < 6 and lastDigit != 0:
        print(f"and is less than 6 and not 0")
else:
    lastDigit = (number * -1) % 10
    print(f"Last digit of {number} is -{lastDigit} ", end="")
    print(f"and is less than 6 and not 0")
