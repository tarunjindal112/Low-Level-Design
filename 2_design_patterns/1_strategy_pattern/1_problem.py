import string
import random
from typing import List


def generate_id(length=8):
    return "".join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:
    id: str
    customer: str
    issue: str

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class CustomerSupport:
    tickets: List[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, processing_strategy: str= "fifo"):
        if len(self.tickets) == 0:
            print("There are no tickets to process. Well Done!")

        if processing_strategy == "fifo":
            for ticket in self.tickets:
                self.process_ticket(ticket)
        elif processing_strategy == "filo":
            for ticket in reversed(self.tickets):
                self.process_ticket(ticket)
        elif processing_strategy == "random":
            list_copy = self.tickets.copy()
            random.shuffle(list_copy)
            for ticket in list_copy:
                self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("========================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("=========================")


app = CustomerSupport()
app.create_ticket("John Smith", "My computer makes srange sounds!!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help!")
app.create_ticket("Argan Egges", "Vscode doesn't solve my bugs automatically")
app.process_tickets("random")

