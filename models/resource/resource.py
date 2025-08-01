from abc import ABC

class Resource(ABC):
    def __init__(self, amount : int = 0) -> None:
        self.__amount = amount
    
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, new_value) -> int:
        if not isinstance(new_value,int):
            raise TypeError("amount must be an int")
        if new_value < 0:
            #TODO MANAGE THE UNDERFLOW OF RESOURCE
            #raise ValueError("amount cant be negative")
            new_value = 0
        self.__amount = new_value
