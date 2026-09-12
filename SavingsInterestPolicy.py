from InterestPolicy import InterestPolicy


class SavingsInterestPolicy(InterestPolicy):

    def calculate(self, balance):
        return balance * 0.04
