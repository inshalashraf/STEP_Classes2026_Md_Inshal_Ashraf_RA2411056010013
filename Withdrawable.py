from abc import ABC, abstractmethod


class Withdrawable(ABC):

    @abstractmethod
    def withdraw(self, amount):
        pass
