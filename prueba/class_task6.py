#!/usr/bin/python3
class Person:
    species = "Homo Sapiens"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

persona = Person("Santi", 27)
print(f"Name : {persona.name}")
print(f"Age: {persona.age}")
print(f"Old Species: {Person.species}")
Person.species = "Homo Sexual"
print(f"New Species: {Person.species}")