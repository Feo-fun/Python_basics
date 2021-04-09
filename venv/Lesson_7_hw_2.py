from abc import ABC, abstractmethod

class Clothes(ABC):
    result = 0
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def tissue_consump(self):
        pass

    def __add__(self, other):
        Clothes.result += self.tissue_consump + other.tissue_consump
        return Suit(0)

    def __str__(self):
        return f'{Clothes.result}'

class Coat(Clothes):

    @property
    def tissue_consump(self):
        return round(self.param / 6.5) + 0.5

class Suit(Clothes):

    @property
    def tissue_consump(self):
        return round((2 * self.param + 0.3) / 100)

coat = Coat(52)
suit = Suit(183)

print(coat + suit)
