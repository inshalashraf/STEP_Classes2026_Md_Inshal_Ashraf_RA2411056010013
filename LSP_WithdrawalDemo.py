from SavingsAccount import SavingsAccount
from CurrentAccount import CurrentAccount
from FixedDepositAccount import FixedDepositAccount


def main():
    accounts = [
        SavingsAccount(301, "Ravi", 21, 5000),
        CurrentAccount(302, "Aman", 25, 8000),
        FixedDepositAccount(303, "Neha", 24, 10000)
    ]

    print("All account types:")
    for account in accounts:
        print(account.get_account_type())

    withdrawable_accounts = [
        SavingsAccount(301, "Ravi", 21, 5000),
        CurrentAccount(302, "Aman", 25, 8000)
    ]

    print("\nWithdrawal from Withdrawable accounts:")
    for account in withdrawable_accounts:
        account.withdraw(100)
        print(account.get_account_type(), "balance:", account.get_balance())

    print("\nFixed Deposit is not included in withdrawal operations.")


if __name__ == "__main__":
    main()
