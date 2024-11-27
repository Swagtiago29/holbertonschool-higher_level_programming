#!/usr/bin/python3

class BankAccount():
    
    def __init__(self, balance = 0):
        self.__balance = balance
    
    def deposit(self, amount = 0):
        if isinstance(amount, int) and amount >= 0:
            self.__balance = self.__balance + amount
        else:
            print("Error: amount not valid")
    def withdraw(self, amount = 0):
        if isinstance(amount, int) and amount >= 0:
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
            else:
                print("Insuficient Funds")
        else:
            print("Error: amount not valid")
    def get_balance(self):
        print(f"Balance: {self.__balance}")

Santi = BankAccount(1000)
Santi.get_balance()
Santi.deposit(200)
Santi.get_balance()
Santi.withdraw(300)
Santi.get_balance()
Santi.withdraw(1500)
Santi.get_balance()