from abc import ABC, abstractmethod

class Facility:
    """
    This abstract class serves as base class for all facilities (production, housing and leisure)
    """
    def __init__(self, name, capacity, integrity = 100):
        self.name = name
        self.capacity = capacity
        self.integrity = integrity

    def repair(self, reparation: int = 10):
        if self.integrity + reparation > 100:
            self.integrity = 100
        else:
            self.integrity += reparation

    def damage(self, damage: int = 10):
        if self.integrity - damage < 0:
            self.integrity = 0
        else:
            self.integrity -= damage