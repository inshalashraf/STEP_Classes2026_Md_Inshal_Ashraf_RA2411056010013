from BankAccount import BankAccount
from AccountRepository import AccountRepository
from NotificationService import NotificationService
from StatementGenerator import StatementGenerator
from SavingsInterestPolicy import SavingsInterestPolicy
from CurrentInterestPolicy import CurrentInterestPolicy


def main():
    account = BankAccount(
        101,
        "Ravi",
        17,
        200,
        "Savings"
    )

    account.deposit(1000)
    account.withdraw(300)
    account.deposit(500)
    account.withdraw(200)

    repository = AccountRepository()
    notification = NotificationService()
    statement_generator = StatementGenerator()

    repository.save(account)
    notification.send("Account transactions completed successfully")

    print(statement_generator.generate(account))

    savings_policy = SavingsInterestPolicy()
    current_policy = CurrentInterestPolicy()

    print("Savings interest: Rs.", savings_policy.calculate(account.get_balance()))
    print("Current interest: Rs.", current_policy.calculate(account.get_balance()))


if __name__ == "__main__":
    main()
