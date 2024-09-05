#!/usr/bin/python3
for i in range(10):
    for u in range(i + 1, 10):
        if i + u == 17:
            print("{}{}".format(i, u))
        else:
            print("{}{}".format(i, u), end=', ')
