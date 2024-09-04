#!/usr/bin/python3
def fizzbuzz():
    for i in range(101):
        if i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz")
            else:
                print("Buzz")
        elif i % 5 == 0:
            print("Fizz")
        else:
            print("{}".format(i))
