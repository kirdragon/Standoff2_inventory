from inventory import Inventory


class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.inventory = Inventory()

    def add_money(self, amount):
        self.balance += amount

    def spend_money(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False
