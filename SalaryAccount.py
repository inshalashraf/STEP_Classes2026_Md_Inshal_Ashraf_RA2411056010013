from BankAccount import BankAccount


class SalaryAccount(BankAccount):

    def __init__(self, account_number, name, age, balance):
        super().__init__(account_number, name, age, balance, "Salary")
