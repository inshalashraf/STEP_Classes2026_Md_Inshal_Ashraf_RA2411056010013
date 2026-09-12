from BankAccount import BankAccount


class FixedDepositAccount(BankAccount):

    def __init__(self, account_number, name, age, balance):
        super().__init__(account_number, name, age, balance, "Fixed Deposit")
