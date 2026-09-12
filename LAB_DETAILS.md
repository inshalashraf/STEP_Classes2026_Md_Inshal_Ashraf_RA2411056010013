# STEP Classes 2026 - Lab Details

## Purpose

This document records the lab scenarios, tasks, design decisions, and checkpoints completed in this repository. It is kept alongside the source code so that the reason behind each class and refactoring is clear.

---

# Section 1 - SRP: BankAccount Does Too Much

## Scenario

GreenLeaf Bank starts with a `BankAccount` class that contains several unrelated responsibilities. The class is responsible for account operations as well as persistence, notifications, statement generation, and other banking services.

## Problem

A class with many unrelated responsibilities has many reasons to change. A change to notification logic, database logic, or statement formatting could require changes to `BankAccount`.

## Solution

The responsibilities were separated into smaller classes:

| File | Responsibility |
|---|---|
| `BankAccount.py` | Account data and basic account operations |
| `AccountRepository.py` | Saving account information |
| `NotificationService.py` | Sending notifications |
| `StatementGenerator.py` | Generating account statements |
| `Main.py` | Demonstrating the design |
| `SRP_WrapUp.txt` | Lab explanation |

## Principle

**Single Responsibility Principle (SRP):** A class should have one clear responsibility and one reason to change.

## Checkpoint

`BankAccount` no longer contains unrelated persistence, notification, or statement-generation responsibilities.

---

# Section 2 - OCP: New Account Types Keep Arriving

## Scenario

GreenLeaf Bank launches Current and Salary Accounts and expects more account types in the future. The interest calculator should not need to be rewritten whenever a new account type is introduced.

## Warm-up

`InterestCalculator.py` shows the original approach using an `if/elif` chain based on the account type.

When a fourth account type is added, the calculator method itself must be edited to add another condition and interest rate. This demonstrates why the original design is difficult to extend.

## Solution

An `InterestPolicy` abstraction was introduced. Each account type can have its own interest-policy class.

| File | Responsibility |
|---|---|
| `InterestCalculator.py` | Warm-up if/else design |
| `InterestPolicy.py` | Common interest-policy contract |
| `SavingsInterestPolicy.py` | Savings interest: 4% |
| `CurrentInterestPolicy.py` | Current interest: 1% |
| `SalaryAccount.py` | Salary account type |
| `SalaryInterestPolicy.py` | Salary interest: 5% |
| `Bank.py` | Uses an injected notification service |
| `SMSNotificationService.py` | Alternative notification implementation |
| `Main.py` | Demonstrates the policies and notification injection |
| `OCP_WrapUp.txt` | Lab explanation |

## Extension Example

Adding `SalaryInterestPolicy` does not require editing `SavingsInterestPolicy.py` or `CurrentInterestPolicy.py`. A new policy is introduced as a new class implementing the existing contract.

## Notification Dependency

`Bank` receives a notification service through its constructor. This allows `NotificationService` and `SMSNotificationService` to be used interchangeably without changing the internal implementation of `Bank`.

## Principle

**Open/Closed Principle (OCP):** Software entities should be open for extension but closed for modification.

## Checkpoint

Adding a new account type or interest rate does not require modifying an existing interest-policy class.

---

# Section 3 - LSP: Fixed Deposit Account Breaks Things

## Scenario

A teammate creates `FixedDepositAccount` as an account type, but early withdrawal is not allowed for a fixed deposit. If every `Account` is assumed to support `withdraw()`, a loop over different account types can fail at runtime.

## Warm-up - Rectangle/Square

`Rectangle.py` provides width, height, and area operations. `Square.py` inherits from `Rectangle` but changes both dimensions whenever either setter is called.

`LSP_Example.py` demonstrates the issue by storing a `Square` in a variable intended for a `Rectangle`, calling `set_width(10)` followed by `set_height(20)`, and observing an area of **400** rather than the expected **200**.

### Why it violates LSP

Calling code assumes that a Rectangle can have its width and height changed independently. Square changes one dimension when the other is changed, so it cannot safely satisfy the behavior expected from the Rectangle abstraction.

## Initial Fixed Deposit Violation

`LSP_BrokenDemo.py` demonstrates the banking problem by putting a Savings account and Fixed Deposit account into the same collection and calling `withdraw()` on both.

The initial design of `FixedDepositAccount` rejects withdrawal with an unsupported-operation exception. The loop therefore crashes when it reaches the Fixed Deposit account.

This is useful as a demonstration of the problem, but it is not the final design.

## Corrected Design

A separate `Withdrawable` contract was introduced.

| Type | Can withdraw? | Implements `Withdrawable`? |
|---|---:|---:|
| `SavingsAccount` | Yes | Yes |
| `CurrentAccount` | Yes | Yes |
| `FixedDepositAccount` | No early withdrawal | No |

Withdrawal-specific code now works with `Withdrawable` objects rather than every `Account`.

This means the caller only receives objects that genuinely support the operation it intends to perform.

## Principle

**Liskov Substitution Principle (LSP):** A subtype must be usable wherever its base type or contract is expected without breaking the assumptions of the calling code.

## Correct Fix

The correct fix is not to make `FixedDepositAccount` implement `Withdrawable` and then throw an exception. That would technically compile but would violate the contract because callers of `Withdrawable` expect withdrawal to be supported.

Instead, `FixedDepositAccount` remains an account, while only accounts that genuinely support withdrawal implement `Withdrawable`.

## Checkpoint

No class in the final design overrides a method merely to throw a "not supported" exception. Types implement only contracts they can honestly fulfill.

---

# Implementation Notes

- Language: **Python 3**
- External libraries: **None required**
- Main concepts: classes, inheritance, abstract base classes, interfaces/contracts, composition, dependency injection, and SOLID principles.
- The assignment's Java-style concepts such as `double`, `extends`, and `UnsupportedOperationException` are represented using Python equivalents where appropriate.
- The code is intentionally kept small and readable for lab evaluation and demonstration.

# Git Workflow

The repository is maintained with small, logical commits. Each commit represents a meaningful lab step such as introducing a class, demonstrating a violation, applying a refactoring, or documenting a checkpoint.

The existing Section 1, Section 2, and Section 3 history is preserved rather than squashing the commits, so the progression of the lab remains visible.

# Future Sections

The repository can continue using the same structure for the remaining SOLID principles:

- Section 4 - Interface Segregation Principle (ISP)
- Section 5 - Dependency Inversion Principle (DIP)

New work should be added without unnecessarily rewriting completed sections.
