#!/usr/bin/python3
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    team_size = 25
    dick_size = "2cm"
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def get_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Team Size: {self.team_size}, Dick Size: {self.dick_size}")

emp = Employee("Jorge", 25000)
emp.get_details()
man = Manager("Mauricio", 50000)
man.get_details()