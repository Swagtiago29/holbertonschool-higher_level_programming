#!/usr/bin/python3

class Flyable:
    def fly(self):
        print("u flying")

class Swimmable:
    def swim(self):
        print("u swimmin")

class Duck(Flyable, Swimmable):
    def what_am_i(self):
        print("imma duck!")

pati = Duck()
pati.swim()
pati.fly()
pati.what_am_i()