from BankAccount import BankAccount
from AccountRepository import AccountRepository
from NotificationService import NotificationService
from StatementGenerator import StatementGenerator


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


if __name__ == "__main__":
    main()
