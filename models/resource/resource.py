from abc import ABC

class Resource(ABC):
    def __init__(self, amount : int = 0):
        self.__amount = amount
    
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, new_value):
        if not isinstance(new_value,int):
            raise TypeError("amount must be an int")
        if new_value < 0:
            raise ValueError("amount cant be negative")
        self.amount = new_value