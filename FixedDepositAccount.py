from BankAccount import BankAccount


class UnsupportedOperationException(Exception):
    pass


class FixedDepositAccount(BankAccount):

    def __init__(self, account_number, name, age, balance):
        super().__init__(account_number, name, age, balance, "Fixed Deposit")

    def withdraw(self, amount):
        raise UnsupportedOperationException("Fixed deposits cannot be withdrawn early")
