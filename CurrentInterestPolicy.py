from InterestPolicy import InterestPolicy


class CurrentInterestPolicy(InterestPolicy):

    def calculate(self, balance):
        return balance * 0.01
