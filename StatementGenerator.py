class StatementGenerator:

    def generate(self, account):
        statement = (
            f"---- Statement for Account #{account.get_account_number()} "
            f"({account.get_name()}) ----\n"
        )

        for entry in account.get_transaction_log():
            statement += entry + "\n"

        statement += f"Current Balance: Rs. {account.get_balance()}\n"
        statement += "-----------------------------------------------------"

        return statement
