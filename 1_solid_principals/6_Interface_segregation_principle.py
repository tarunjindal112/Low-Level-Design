from abc import ABC, abstractmethod


class Order:
    items: list = []
    quantities: list = []
    prices: list = []
    status: str = "open"

    def add_item(self, name: str, quantity: int, price: int):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]

        return total


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order:Order):
        pass


class PaymentProcessor_SMS(PaymentProcessor):
    @abstractmethod
    def auth_sms(self, code: str):
        pass


class DebitPaymentProcessor(PaymentProcessor_SMS):
    def __init__(self, security_code: str):
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code: str):
        print(f"Verifying sms code {code}")
        self.verified = True

    def pay(self, order:Order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str):
        self.security_code = security_code

    def pay(self, order:Order):
        print("Processing debit payment type")
        print(f"Verifying security code {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor_SMS):
    def __init__(self, email_address: str):
        self.email_address = email_address
        self.verified = False

    def auth_sms(self, code: str):
        print(f"Verifying sms code {code}")
        self.verified = True

    def pay(self, order:Order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Verifying email address {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("keyboard", 1, 50)
order.add_item("ssd", 1, 150)
order.add_item("USB Cable", 2, 5)

print(order.total_price())
payment_processor = CreditPaymentProcessor("0372846")
payment_processor.pay(order)







