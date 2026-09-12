# STEP Classes 2026 - SOLID Principles Lab

**Student:** Md. Inshal Ashraf  
**Program:** B.Tech CSE (Data Science)  
**Semester:** 5th Semester  
**Repository:** STEP Classes 2026

## About This Repository

This repository contains the practical lab work for the STEP Classes 2026 course, implemented in Python.

The exercises use a GreenLeaf Bank example to understand the **SOLID principles** through small, progressive refactoring tasks.

The code is intentionally kept simple and readable so that each design principle can be identified from the implementation.

## Lab Progress

| Section | Principle | Scenario | Status |
|---|---|---|---|
| 1 | **SRP** - Single Responsibility Principle | BankAccount is doing too many jobs | Completed |
| 2 | **OCP** - Open/Closed Principle | New account types and interest rates keep arriving | Completed |
| 3 | **LSP** - Liskov Substitution Principle | Fixed Deposit account breaks withdrawal operations | Completed |
| 4 | **ISP** - Interface Segregation Principle | To be added | Pending |
| 5 | **DIP** - Dependency Inversion Principle | To be added | Pending |

## Section 1 - SRP

### Scenario

The original `BankAccount` class was responsible for account operations, database work, notifications, statement generation, PIN handling, interest calculation, and account lifecycle operations.

### Refactoring

The responsibilities were separated into focused classes:

- `BankAccount.py` - account data and basic account operations
- `AccountRepository.py` - persistence responsibility
- `NotificationService.py` - notification responsibility
- `StatementGenerator.py` - statement generation responsibility
- `Main.py` - example usage
- `SRP_WrapUp.txt` - explanation of the refactoring

### Result

`BankAccount` now has a focused responsibility instead of handling unrelated services.

## Section 2 - OCP

### Scenario

GreenLeaf Bank introduced Savings, Current, and Salary accounts. The interest calculation should allow new account types without repeatedly modifying existing interest-policy classes.

### Implementation

- `InterestCalculator.py` - warm-up example showing the original if/else design
- `InterestPolicy.py` - common interest policy abstraction
- `SavingsInterestPolicy.py` - 4% interest
- `CurrentInterestPolicy.py` - 1% interest
- `SalaryAccount.py` - Salary account type
- `SalaryInterestPolicy.py` - 5% interest
- `Bank.py` - accepts a notification service through its constructor
- `SMSNotificationService.py` - second notification implementation
- `Main.py` - demonstrates the policies and dependency injection
- `OCP_WrapUp.txt` - explanation of the OCP result

### Checkpoint

Adding a new account type or interest rate does not require editing an existing interest-policy class.

## Section 3 - LSP

### Scenario

A Fixed Deposit account cannot support early withdrawal. Treating it like every other account and forcing it to provide `withdraw()` causes the calling code to fail.

### Warm-up

The classic Rectangle/Square example demonstrates the LSP problem:

- `Rectangle.py` - base Rectangle abstraction
- `Square.py` - Square implementation
- `LSP_Example.py` - demonstrates the unexpected area of 400 instead of 200

### Initial Violation

- `FixedDepositAccount.py` - Fixed Deposit account used in the initial LSP-violation demonstration
- `LSP_BrokenDemo.py` - attempts withdrawal through a list of accounts and demonstrates the failure

### Corrected Design

- `Withdrawable.py` - withdrawal contract
- `SavingsAccount.py` - implements `Withdrawable`
- `CurrentAccount.py` - implements `Withdrawable`
- `FixedDepositAccount.py` - remains an account but is not withdrawable
- `LSP_WrapUp.txt` - explains the substitution rule and the fix

### Checkpoint

No class should override a method only to throw a "not supported" exception. A type should implement only contracts it can genuinely fulfill.

## Project Structure

```text
STEP_Classes2026_Md_Inshal_Ashraf_RA2411056010013/
│
├── README.md
├── LAB_DETAILS.md
│
├── BankAccount.py
├── AccountRepository.py
├── NotificationService.py
├── StatementGenerator.py
├── SRP_WrapUp.txt
│
├── InterestCalculator.py
├── InterestPolicy.py
├── SavingsInterestPolicy.py
├── CurrentInterestPolicy.py
├── SalaryAccount.py
├── SalaryInterestPolicy.py
├── Bank.py
├── SMSNotificationService.py
├── OCP_WrapUp.txt
│
├── Rectangle.py
├── Square.py
├── LSP_Example.py
├── FixedDepositAccount.py
├── LSP_BrokenDemo.py
├── Withdrawable.py
├── SavingsAccount.py
├── CurrentAccount.py
└── LSP_WrapUp.txt
```

## Running the Examples

The project uses only standard Python features and does not require external packages.

From the repository directory, run the relevant example with Python 3:

```bash
python Main.py
python LSP_Example.py
python LSP_BrokenDemo.py
```

`Main.py` contains the combined GreenLeaf Bank examples from the completed SRP and OCP work. The LSP examples are kept in separate files so that the problem and its corrected design can be studied independently.

## Design Principles Covered

### SRP

A class should have one clear responsibility and one main reason to change.

### OCP

Software entities should be open for extension but closed for modification. New interest policies are added as new classes instead of changing existing policy classes.

### LSP

A subtype should be usable wherever its abstraction is expected without breaking the assumptions of the calling code. The `Withdrawable` interface ensures that only accounts capable of withdrawal are passed to withdrawal-specific code.

## Development Approach

The lab is developed incrementally. Each meaningful lab task is recorded as a separate Git commit so the progression from the original design, through the problem, to the refactored solution remains visible in the repository history.

## Current Status

**Completed:** Sections 1-3  
**Next:** Section 4 - Interface Segregation Principle (ISP)
