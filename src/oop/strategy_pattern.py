from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount: int):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card")


class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paying {amount} using PayPal")


class NotPayment(Payment):
    def pay(self, amount: int):
        print("Do not pay")


class Trash:
    pass


class PaymentController:
    def __init__(self, service: Payment):
        self.service = service

    def use_service(self):
        self.service.pay(50)


payment_controller = PaymentController(NotPayment())
payment_controller.use_service()
