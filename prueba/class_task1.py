#!/usr/bin/python3
class Car:
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"[Brand:{self.brand}] [Model:{self.model}] [Year:{self.year}]")

car1 = Car("BMW", "viejardo", "1995")
car1.display_info()