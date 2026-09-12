class BankAccount:

    # Job: manage the bank account's basic operations like deposit, withdrawal and balance.

    def __init__(self, account_number, name, age, balance, account_type):

        # Keep the basic account rules here.
        if age < 18:
            age = 18

        minimum_balance = 500.0 if account_type == "Savings" else 1000.0

        if balance < minimum_balance:
            balance = minimum_balance

        self.account_number = account_number
        self.name = name
        self.age = age
        self.balance = balance
        self.account_type = account_type
        self.status = "Active"
        self.transaction_log = []

    def deposit(self, amount):

        if self.status != "Active":
            print("Account is not active")
            return False

        if amount <= 0:
            print("Invalid deposit amount")
            return False

        self.balance += amount
        self.transaction_log.append(
            f"DEPOSIT: Rs. {amount} | New balance: {self.balance}"
        )

        return True

    def withdraw(self, amount):

        if self.status != "Active":
            print("Account is not active")
            return False

        if amount <= 0:
            print("Invalid withdrawal amount")
            return False

        minimum_balance = 500.0 if self.account_type == "Savings" else 1000.0

        if self.balance - amount < minimum_balance:
            print("Withdrawal would breach minimum balance")
            return False

        self.balance -= amount
        self.transaction_log.append(
            f"WITHDRAW: Rs. {amount} | New balance: {self.balance}"
        )

        return True

    # Simple getters
    def get_account_number(self):
        return self.account_number

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_balance(self):
        return self.balance

    def get_status(self):
        return self.status

    def get_account_type(self):
        return self.account_type

    def get_transaction_log(self):
        return self.transaction_log
