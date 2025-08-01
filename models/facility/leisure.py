from models.facility.facility import Facility
from tools.constants import *
import random

class Leisure(Facility):
    def __init__(self, name: str = "Leisure", capacity: int = LEISURE_DEFAULT_CAPACITY):
        super().__init__(name, capacity)
        self.__users = []

    @property
    def users(self) -> list("Citizen"):
        return self.__users
    
    @property
    def is_full(self) -> bool:
        return len(self.users) >= self.capacity
    
    def grow(self, electricity: "Electricity", water: "Water", is_night: bool) -> None:
        # damage caused by users
        damage = round(self.users * DAMAGE_DAILY_PER_LEISURE_USER)
        # all users leave the leisure facility at end of day or night
        self.users = []
        if not is_night:
            # 'natural' damage, once in 24h
            damage += random.randint(0, DAMAGE_MAX_DAILY_LEISURE)

        # apply damage
        super().grow(damage)
    
    def add_user(citizen):
        if len(self.__users) == self.capacity:
            raise Exception("This leisure facility is full already")
        
        self.users.append(citizen)
