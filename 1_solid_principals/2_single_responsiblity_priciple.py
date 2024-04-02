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


class PaymentProcessor:
    def pay_debit(self, order: Order, security_code: str):
        print("Processing debit payment type")
        print(f"Verifying security code {security_code}")
        order.status = "paid"

    def pay_credit(self, order: Order, security_code: str):
        print("Processing debit payment type")
        print(f"Verifying security code {security_code}")
        order.status = "paid"


order = Order()
order.add_item("keyboard", 1, 50)
order.add_item("ssd", 1, 150)
order.add_item("USB Cable", 2, 5)

print(order.total_price())
payment_processor = PaymentProcessor()
payment_processor.pay_debit(order, "0372846")





