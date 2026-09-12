from BankAccount import BankAccount
from AccountRepository import AccountRepository
from NotificationService import NotificationService
from StatementGenerator import StatementGenerator
from SavingsInterestPolicy import SavingsInterestPolicy
from CurrentInterestPolicy import CurrentInterestPolicy
from SalaryAccount import SalaryAccount
from SalaryInterestPolicy import SalaryInterestPolicy
from Bank import Bank
from SMSNotificationService import SMSNotificationService


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

    bank = Bank(notification)
    bank.notify_account("Account transactions completed successfully")

    print(statement_generator.generate(account))

    savings_policy = SavingsInterestPolicy()
    current_policy = CurrentInterestPolicy()

    print("Savings interest: Rs.", savings_policy.calculate(account.get_balance()))
    print("Current interest: Rs.", current_policy.calculate(account.get_balance()))

    salary_account = SalaryAccount(102, "Aman", 25, 10000)
    salary_policy = SalaryInterestPolicy()

    print("Salary interest: Rs.", salary_policy.calculate(salary_account.get_balance()))

    # The Bank can use another notification service without changing Bank.py.
    sms_bank = Bank(SMSNotificationService())
    sms_bank.notify_account("Salary account created")


if __name__ == "__main__":
    main()
