from models.facility.facility import Facility
from models.citizen.citizen import Citizen
from tools.constants import *
import random

class Housing(Facility):
    def __init__(self, name: str = "Housing", capacity: int = HOUSING_DEFAULT_CAPACITY):
        super().__init__(name, capacity)
        self.__inhabitants = []

    @property
    def inhabitants(self) -> list("Citizen"):
        return self.__inhabitants
    
    @property
    def is_full(self) -> bool:
        return len(self.inhabitants) >= self.capacity

    def add_inhabitant(self, citizen):
        if not isinstance(citizen, Citizen):
            raise TypeError("Only citizens can be added as housing inhabitants")
        if len(self.__inhabitants) == self.capacity:
            raise Exception("This housing is full already")

        if self.capacity > len(self.__inhabitants):
            self.inhabitants.append(citizen)
    
    def grow(self, electricity: "Electricity", water: "Water", is_night: bool) -> None:
        electricity_loss = random.randint(MIN_ELECTRICITY_LOSS_DAILY_HOUSING, self.inhabitants * 2)
        electricity.amount -= electricity_loss
        damage = round(self.inhabitants * DAMAGE_DAILY_PER_HOUSING_INHABITANT)
        super().grow(damage)