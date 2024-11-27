#!/usr/bin/python3
import math

class Shape:

    def area():
        raise(NotImplementedError)

class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius **2
    
class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

def print_area(shape):
    print(f"Area of shape is: {shape.area()}")

cir = Circle(5)
rec = Rectangle(4, 6)
print_area(cir)
print_area(rec)