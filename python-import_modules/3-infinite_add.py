#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    x = len(argv)
    if x == 1:
        print("0")
    elif x == 2:
        print("{}".format(int(argv[1])))
    else:
        y = 0
        for i in range(1, x):
            y += int(argv[i])
        print("{}".format(y))
