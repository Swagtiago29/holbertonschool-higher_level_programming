#!/usr/bin/python3
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def process_payment(self):
        pass

class CreditCardPayment(Payment):
    def process_payment(self):
        return "sisi, pagaste con Tarjeta!"

class PayPalPayment(Payment):
    def process_payment(self):
        return "opa, pagaste con PayPal!"

tarjetazo = CreditCardPayment()
paypal = PayPalPayment()
print(tarjetazo.process_payment())
print(paypal.process_payment())