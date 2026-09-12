from InterestPolicy import InterestPolicy


class SalaryInterestPolicy(InterestPolicy):

    def calculate(self, balance):
        return balance * 0.05
