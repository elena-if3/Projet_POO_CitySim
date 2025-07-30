from abc import ABC, abstractmethod

class Facility:
    """
    This abstract class serves as base class for all facilities (production, housing and leisure)
    """
    def __init__(self, name: str, capacity: int):
        self.__name = name
        self.__capacity = capacity
        self.__integrity = 100

    @property
    def name(self):
        return self.__name

    @property
    def capacity(self):
        return self.__capacity

    @property
    def integrity(self):
        return self.__integrity

    def repair(self, reparation: int = 10):
        if not isinstance(reparation, int):
            raise TypeError("Level of reparation must be an integer")
        if reparation < 0 or reparation > 100:
            raise ValueError("Level of reparation must be between 0 and 100 (%)")

        if self.__integrity + reparation > 100:
            self.__integrity = 100
        else:
            self.__integrity += reparation

    def damage(self, damage: int = 10):
        if not isinstance(damage, int):
            raise TypeError("Level of damage must be an integer")
        if damage < 0 or damage > 100:
            raise ValueError("Level of damage must be between 0 and 100 (%)")

        if self.__integrity - damage < 0:
            self.__integrity = 0
        else:
            self.__integrity -= damage
