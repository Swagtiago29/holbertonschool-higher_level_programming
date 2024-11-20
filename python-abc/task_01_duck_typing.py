#!/usr/bin/python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area():
        pass
    @abstractmethod
    def perimeter():
        pass
class Circle(Shape):
    def __init__(self, radius):
            if radius <= 0:
                 raise ValueError("radius should be a positive number")
            self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        return math.pi * 2 * self.radius
class Rectangle(Shape):
    def __init__(self, width, height):
            self.width = width
            self.height = height
    def area(self):
        return self.height * self.width
    def perimeter(self):
        return 2 * (self.height + self.width)
def shape_info(Shape):
    print(f"Area: {Shape.area()}")
    print(f"Permeter: {Shape.perimeter()}")