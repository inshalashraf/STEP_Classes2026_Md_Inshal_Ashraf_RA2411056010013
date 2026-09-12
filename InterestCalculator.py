class InterestCalculator:

    def calculate(self, balance, account_type):
        # To add a 4th account type, I would have to edit this method.
        # I would add another elif condition for the new account type.
        # I would also add the new interest rate in this if/else chain.
        # So the calculator itself has to be changed every time a new type is added.

        if account_type == "Savings":
            return balance * 0.04
        elif account_type == "Current":
            return balance * 0.01
        else:
            return 0.0
