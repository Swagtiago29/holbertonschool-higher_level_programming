#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 0:
        print("0 arguments.")
    elif len(argv) == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(argv)))
        for argv in range(len(argv)):
            print("{}: {}".format(len(argv), argv[0]))