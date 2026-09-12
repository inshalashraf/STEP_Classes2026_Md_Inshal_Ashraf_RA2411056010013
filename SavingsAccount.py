from BankAccount import BankAccount
from Withdrawable import Withdrawable


class SavingsAccount(BankAccount, Withdrawable):

    def __init__(self, account_number, name, age, balance):
        super().__init__(account_number, name, age, balance, "Savings")

    def withdraw(self, amount):
        return super().withdraw(amount)
