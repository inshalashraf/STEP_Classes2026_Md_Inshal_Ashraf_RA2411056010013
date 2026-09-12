# Initial LSP test observation:
# A list of Account objects contained a SavingsAccount and a FixedDepositAccount.
# The withdrawal loop worked for the SavingsAccount but crashed on the FixedDepositAccount
# because its withdraw() implementation raised UnsupportedOperationException.
# This showed that FixedDepositAccount could not safely be substituted for Account
# when the calling code assumed every Account supported withdrawal.

print("Observed crash: FixedDepositAccount withdrawal raised UnsupportedOperationException.")
print("This was fixed by introducing the Withdrawable interface.")
