from abc import ABC, abstractmethod

class Facility:
    """
    This abstract class serves as base class for all facilities (production, housing and leisure)
    """
    def __init__(self, name, capacity, integrity = 100):
        self.__name = name
        self.__capacity = capacity
        self.__integrity = integrity

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
        if self.__integrity + reparation > 100:
            self.__integrity = 100
        else:
            self.__integrity += reparation

    def damage(self, damage: int = 10):
        if self.__integrity - damage < 0:
            self.__integrity = 0
        else:
            self.__integrity -= damage