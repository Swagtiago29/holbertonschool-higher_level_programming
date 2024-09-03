#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of"
str2 = "and is greater than 5"
str3 = "and is less than 6 and not 0"
ld = abs(number) % 10

if number < 0:
    if ld == 0: 
        print(f"{str1} {number} is -{ld} and is zero")
    else:
        print(f"{str1} {number} is -{ld} {str3}")
else:
    if ld > 5:
        print(f"{str1} {number} is {ld} {str2}")
    elif ld == 0: 
        print(f"{str1} {number} is {ld} and is zero")
    else:
        print(f"{str1} {number} is {ld} {str3}")