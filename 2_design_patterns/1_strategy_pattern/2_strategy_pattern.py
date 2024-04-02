import string
import random
from typing import List
from abc import ABC, abstractmethod


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


class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, tickets_list: List[SupportTicket]) -> List[SupportTicket]:
        pass


class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets_list: List[SupportTicket]) -> List[SupportTicket]:
        return tickets_list.copy()


class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets_list: List[SupportTicket]) -> List[SupportTicket]:
        tickets_list_copy = tickets_list.copy()
        tickets_list_copy.reverse()
        return tickets_list_copy


class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets_list: List[SupportTicket]) -> List[SupportTicket]:
        tickets_list_copy = tickets_list.copy()
        random.shuffle(tickets_list_copy)
        return tickets_list_copy


class CustomerSupport:
    tickets: List[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, processing_strategy: TicketOrderingStrategy):
        if len(self.tickets) == 0:
            print("There are no tickets to process. Well Done!")

        ticket_list = processing_strategy.create_ordering(self.tickets)

        for ticket in ticket_list:
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
app.process_tickets(RandomOrderingStrategy())

