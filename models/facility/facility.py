from abc import ABC, abstractmethod

class Facility(ABC):
    """
    This abstract class serves as base class for all facilities (factory, housing and leisure)
    """
    def __init__(self, name: str, capacity: int) -> None:
        self.__name = name
        self.__capacity = capacity
        self.__integrity = 100

    @property
    def name(self) -> str:
        return self.__name

    @property
    def capacity(self) -> int:
        return self.__capacity

    @property
    def integrity(self) -> int:
        return self.__integrity

    def repair(self, reparation: int) -> None:
        if not isinstance(reparation, int):
            raise TypeError("Level of reparation must be an integer")
        if reparation < 0 or reparation > 100:
            raise ValueError("Level of reparation must be between 0 and 100 (%)")

        if self.__integrity + reparation > 100:
            self.__integrity = 100
        else:
            self.__integrity += reparation

    def damage(self, damage: int) -> None:
        if not isinstance(damage, int):
            raise TypeError("Level of damage must be an integer")
        if damage < 0 or damage > 100:
            raise ValueError("Level of damage must be between 0 and 100 (%)")

        if self.__integrity - damage < 0:
            self.__integrity = 0
        else:
            self.__integrity -= damage
    
    def grow(self, damage: int):
        self.damage -= damage
