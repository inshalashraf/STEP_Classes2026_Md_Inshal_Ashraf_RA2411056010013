from BankAccount import BankAccount
from FixedDepositAccount import FixedDepositAccount


def main():
    accounts = [
        BankAccount(201, "Ravi", 21, 5000, "Savings"),
        FixedDepositAccount(202, "Aman", 25, 10000)
    ]

    print("Trying withdrawal from every Account:")
    for account in accounts:
        print("Withdrawing from", account.get_account_type())
        account.withdraw(100)


if __name__ == "__main__":
    main()
