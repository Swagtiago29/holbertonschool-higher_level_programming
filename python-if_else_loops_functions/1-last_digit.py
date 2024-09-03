#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_number = number % 10
    if last_number > 5:
        str = f"Last digit of {number} is {last_number} and is greater than 5"
    else:
        str = f"Last digit of {number} is {last_number} and is \
    less than 6 and not 0"
if number < 0:
    last_number = abs(number) % 10
    str = f"Last digit of {number} is -{last_number} and is \
less than 6 and not 0"
else:
    str = f"Last digit of {number} is {last_number} and is 0"
print (f"{str}")