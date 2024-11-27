#!/usr/bin/python3

class Calculator:
    
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def create_default(cls):
        return cls()
    
print(Calculator.add(9, 1))
print(Calculator.create_default())