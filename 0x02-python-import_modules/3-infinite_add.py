#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    addition = 0

    for i in range(1, len(sys.argv)):
        addition = addition + int(sys.argv[i])

    print(addition)
