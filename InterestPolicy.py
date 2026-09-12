from abc import ABC, abstractmethod


class InterestPolicy(ABC):

    @abstractmethod
    def calculate(self, balance):
        pass
