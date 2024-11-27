#!/usr/bin/python3

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def make_sound(self):
        print("Animal noise!")

class Dog(Animal):
    def make_sound(self):
        print("Bark!")

ani = Animal("Conejo", "conejis conujus")
ani.make_sound()
perris = Dog("Mario", "perro")
perris.make_sound()